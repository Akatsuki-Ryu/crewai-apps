from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
import requests, os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.retrievers import BaseRetriever

from langchain_openai import OpenAIEmbeddings
embedding_function = OpenAIEmbeddings()
from langchain_community.embeddings import OllamaEmbeddings
# embeddings = OllamaEmbeddings()
embeddings = OllamaEmbeddings(model=os.environ["OPENAI_MODEL_NAME"])


# Tool 1 : Save the news articles in a database
class SearchNewsDB:
    @tool("News DB Tool")
    def news(query: str):
        """Fetch news articles and process their contents."""
        API_KEY = os.getenv('NEWSAPI_KEY')  # Fetch API key from environment variable
        base_url = "https://newsapi.org/v2/everything"
        print(f"Searching for news on query...", query)


        params = {
            'q': query,
            'sortBy': 'publishedAt',
            'apiKey': API_KEY,
            'language': 'en',
            'pageSize': 5,
        }

        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print("Failed to retrieve news.")
            return "Failed to retrieve news."

        articles = response.json().get('articles', [])
        print(f"Found {len(articles)} articles.")
        all_splits = []
        for article in articles:
            # Assuming WebBaseLoader can handle a list of URLs
            loader = WebBaseLoader(article['url'])
            docs = loader.load()
            print(f"Loaded {len(docs)} documents from {article['url']}.")
            # print(docs)

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(docs)
            all_splits.extend(splits)  # Accumulate splits from all articles

        # Index the accumulated content splits if there are any
        if all_splits:
            vectorstore = Chroma.from_documents(all_splits, embedding=embeddings,
                                                persist_directory="./chroma_db")
            retriever = vectorstore.similarity_search(query)
            print(f"Found {len(retriever)} relevant articles.")
            # print(retriever)
            return retriever
        else:
            print("No content available for processing.")
            return "No content available for processing."


# Tool 2 : Get the news articles from the database
class GetNews:
    @tool("Get News Tool")
    def news(query: str) -> str:
        """Search Chroma DB for relevant news information based on a query."""
        vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
        retriever = vectorstore.similarity_search(query)
        print(f"FROM DATABASE Found {len(retriever)} relevant articles. about {query}")
        print(retriever)
        return retriever


# Tool 3 : Search for news articles on the web
search_tool = DuckDuckGoSearchRun()