# pip install crewai langchain-community langchain-openai requests duckduckgo-search chromadb

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_core.retrievers import BaseRetriever
from langchain_openai import OpenAIEmbeddings

from tools import SearchNewsDB, GetNews, search_tool

embedding_function = OpenAIEmbeddings()


# llm = ChatOpenAI(model="gpt-3.5-turbo")



# 2. Creating Agents
news_search_agent = Agent(
    role='News Seacher',
    goal='Generate key points for each news article from the latest news,',
    backstory='Expert in analysing and generating key points from news content for quick updates.',
    tools=[SearchNewsDB().news],
    allow_delegation=False,
    verbose=True,
    # llm=llm
)

writer_agent = Agent(
    role='Writer',
    goal='Identify all the topics received. Use the Get News Tool to verify the each topic to search. Use the Search tool for detailed exploration of each topic. Summarise the retrieved information in depth for every topic.',
    backstory='Expert in crafting engaging narratives from complex information.',
    tools=[GetNews().news, search_tool],
    allow_delegation=True,
    verbose=True,
    # llm=llm
)

# 3. Creating Tasks
news_search_task = Task(
    description='Search for xiaomi new car SU7 and create key points for each news.',
    agent=news_search_agent,
    expected_output='Key points for each news article from the latest news.',
    tools=[SearchNewsDB().news]
)

writer_task = Task(
    description=f"""
    Go step by step.
    Step 1: Identify all the topics received.
    Step 2: Use the Get News Tool to verify the each topic by going through one by one.
    Step 3: Use the Search tool to search for information on each topic one by one. 
    Step 4: Go through every topic and write an in-depth summary of the information retrieved.
    Don't skip any topic.
    """,
    agent=writer_agent,
    context=[news_search_task],
    expected_output='Summarised information for every topic.',
    tools=[GetNews().news, search_tool]
)

# 4. Creating Crew
news_crew = Crew(
    agents=[news_search_agent, writer_agent],
    tasks=[news_search_task, writer_task],
    process=Process.sequential,
    # manager_llm=llm
)

# Execute the crew to see RAG in action
result = news_crew.kickoff()
print(result)
