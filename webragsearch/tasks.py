from crewai import Agent, Task, Crew, Process
from agents import NewsAgentsclass
from tools import SearchNewsDB, GetNews, search_tool

agentsobj = NewsAgentsclass()
news_search_agent = agentsobj.news_search_agent
writer_agent = agentsobj.writer_agent


# 3. Creating Tasks
class NewsTasksclass:
    def __init__(self, search_topic, news_search_agent, writer_agent):
        self.news_search_task = self.create_news_search_task(search_topic, news_search_agent)
        self.writer_task = self.create_writer_task(writer_agent)

    def create_news_search_task(self, search_topic, news_search_agent):
        return Task(
            description=f'Search for {search_topic} and create key points for each news. make sure to check with human if the collected key points are correct.',
            agent=news_search_agent,
            expected_output='Key points for each news article from the latest news.',
            tools=[SearchNewsDB().news, search_tool],
            human_input=True
        )

    def create_writer_task(self, writer_agent):
        return Task(
            description=f"""
            Go step by step.
            Step 1: Identify all the topics received.
            Step 2: Use the Get News Tool to verify the each topic by going through one by one.
            Step 3: Use the Search tool to search for information on each topic one by one. 
            Step 4: Go through every topic and write an in-depth summary of the information retrieved.
            Don't skip any topic.
            """,
            agent=writer_agent,
            context=[self.news_search_task],
            expected_output='Show the information for each step and also information of every topic.',
            tools=[GetNews().news, search_tool],
            human_input=True
        )
