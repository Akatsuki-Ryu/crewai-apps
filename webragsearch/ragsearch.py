# pip install crewai langchain-community langchain-openai requests duckduckgo-search chromadb

from crewai import Agent, Task, Crew, Process

from tools import SearchNewsDB, GetNews, search_tool
from agents import NewsAgentsclass
from tasks import NewsTasksclass


class NewsCrewclass:
    def __init__(self):
        self.agentsobj = NewsAgentsclass()
        self.news_search_agent = self.agentsobj.news_search_agent
        self.writer_agent = self.agentsobj.writer_agent

        self.tasksobj = NewsTasksclass(self.news_search_agent, self.writer_agent)
        self.news_search_task = self.tasksobj.news_search_task
        self.writer_task = self.tasksobj.writer_task

    def run(self):
        crewinst = Crew(
            agents=[self.news_search_agent, self.writer_agent],
            tasks=[self.news_search_task, self.writer_task],
            process=Process.sequential,
            # manager_llm=llm
            verbose=True
        )
        result = crewinst.kickoff()
        return result


if __name__ == "__main__":
    print("## RAG Crew")
    print('-------------------------------')
    crewobj = NewsCrewclass()
    news_crew = crewobj.run()
    # Execute the crew to see RAG in action
    print(news_crew)