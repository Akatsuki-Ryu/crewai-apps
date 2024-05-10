# pip install crewai langchain-community langchain-openai requests duckduckgo-search chromadb

from crewai import Agent, Task, Crew, Process

from agents import NewsAgentsclass
from tasks import NewsTasksclass


class NewsCrewclass:
    def __init__(self, search_topic):
        self.agentsobj = NewsAgentsclass()
        self.news_search_agent = self.agentsobj.news_search_agent
        self.writer_agent = self.agentsobj.writer_agent

        self.tasksobj = NewsTasksclass(search_topic, self.news_search_agent, self.writer_agent)
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

    search_topic = input("What is search topic?\n")
    if not search_topic:
        search_topic = "Artificial Intelligence in 2024"
    crewobj = NewsCrewclass(search_topic)
    news_crew = crewobj.run()
    # Print results
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print(news_crew)
