from crewai import Agent, Task, Crew, Process
from agents import NewsAgents
from tools import search_tool, SearchNewsDB, GetNews

agentsobj = NewsAgents()
news_search_agentobj = agentsobj.news_search_agent
writer_agentobj = agentsobj.writer_agent


# 3. Creating Tasks
class NewsTasks:
    def __init__(self, news_search_agent, writer_agent):
        self.news_search_agent = news_search_agentobj
        self.writer_agent = writer_agentobj

    def create_news_search_task(self):
        return Task(
            description='Search for AI 2024 and create key points for each news.',
            agent=self.news_search_agent,
            expected_output='Key points for each news article from the latest news.',
            tools=[SearchNewsDB().news]
        )

    def create_writer_task(self):
        return Task(
            description=f"""
            Go step by step.
            Step 1: Identify all the topics received.
            Step 2: Use the Get News Tool to verify the each topic by going through one by one.
            Step 3: Use the Search tool to search for information on each topic one by one. 
            Step 4: Go through every topic and write an in-depth summary of the information retrieved.
            Don't skip any topic.
            """,
            agent=self.writer_agent,
            context=[self.create_news_search_task()],
            expected_output='Summarised information for every topic.',
            tools=[GetNews().news, search_tool]
        )
