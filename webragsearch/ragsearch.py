# pip install crewai langchain-community langchain-openai requests duckduckgo-search chromadb

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_core.retrievers import BaseRetriever

from agents import NewsAgentsclass
from tasks import NewsTasksclass


# 4. Creating Crew
class NewsCrew:
    def __init__(self, search_topic):
        # self.agents = agents
        # self.tasks = tasks
        # self.process = process
        # self.crew = None
        self.search_topic = search_topic

    def create_crew(self):
        self.crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=self.process,
            # manager_llm=llm
        )

    def run(self):
        # if self.crew is None:
        #     raise Exception("Crew is not created. Call create_crew() first.")

        agentsobj = NewsAgentsclass()
        news_search_agentobj = agentsobj.news_search_agent
        writer_agentobj = agentsobj.writer_agent

        tasksobj = NewsTasksclass(news_search_agentobj, writer_agentobj)
        news_search_taskobj = tasksobj.create_news_search_task(self.search_topic)
        writer_taskobj = tasksobj.create_writer_task(self.search_topic)

        news_crew_obj = Crew(
            agents=[news_search_agentobj, writer_agentobj],
            tasks=[news_search_taskobj, writer_taskobj],
            # process=Process.sequential,
            verbose=True
        )
        # news_crew_obj.create_crew()
        result = news_crew_obj.kickoff()
        return result


if __name__ == "__main__":
    print("##Running Rag search Crew\n")
    print('-------------------------------')
    search_topic = input("Enter the search topic: ")
    # if there is no imput , setup a default search topic
    if search_topic == "":
        search_topic = "Xiaomi new car SU7"
    # define a crew object
    news_crew_obj = NewsCrew(search_topic)
    # Get your crew to work!
    result = news_crew_obj.run()
    print("###################### result ######################")
    print(result)
