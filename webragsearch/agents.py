from crewai import Agent, Task, Crew, Process

from tools import SearchNewsDB, GetNews, search_tool

from langchain_openai import ChatOpenAI
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
