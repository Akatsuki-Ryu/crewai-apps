
from crewai import Agent, Task, Crew, Process
from tools import search_tool, SearchNewsDBclass, GetNewsclass


# llm = ChatOpenAI(model="gpt-3.5-turbo")

# 2. Creating Agents
class NewsAgentsclass:
    def __init__(self):
        self.news_search_agent = self.create_news_search_agent()
        self.writer_agent = self.create_writer_agent()

    def create_news_search_agent(self):
        return Agent(
            role='News Seacher',
            goal='Generate key points for each news article from the latest news',
            backstory='Expert in analysing and generating key points from news content for quick updates.',
            tools=[SearchNewsDBclass().news],
            allow_delegation=True,
            verbose=True,
            # llm=llm
        )

    def create_writer_agent(self):
        return Agent(
            role='Writer',
            goal='Identify all the topics received. Use the Get News Tool to verify the each topic to search. Use the Search tool for detailed exploration of each topic. Summarise the retrieved information in depth for every topic.',
            backstory='Expert in crafting engaging narratives from complex information.',
            tools=[GetNewsclass().news, search_tool],
            allow_delegation=True,
            verbose=True,
            # llm=llm
        )
