import os
from crewai import Agent, Task, Crew, Process
from agents import websearchtoolboxagentsclass
from tasks import websearchtoolboxtasksclass

from langchain_community.llms import Ollama

# this is managed by the main.py
# model_name = os.getenv("OPENAI_MODEL_NAME")
# base_url = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
# base_url = os.getenv("OPENAI_API_BASE")

os.environ["SERPER_API_KEY"] = 'c7a06bdaa06e509b2116cb12ddb60fb773c9693f'


# Initialize the Ollama model with the specified model and base URL
# ollama_model = Ollama(model=model_name, base_url=base_url)

### OPENAI
# os.environ["OPENAI_API_KEY"] = "Your Key"
# export OPENAI_API_KEY=sk-blablabla # on Linux/Mac


class websearchcrewclass:
    def __init__(self, var1):
        self.var1 = var1
        pass

    def run(self):
        agentsobj = websearchtoolboxagentsclass()
        tasksobj = websearchtoolboxtasksclass()

        agent1 = agentsobj.infoseeker_agent()
        agent2 = agentsobj.legalesebot_agent()
        agent3 = agentsobj.guardian_agent()
        agent4 = agentsobj.sciWritAI_agent()

        task1 = tasksobj.task_1_name(agent1, self.var1)
        task2 = tasksobj.task_2_name(agent2, self.var1, self.var1)

        crew = Crew(
            agents=[agent1, agent2, agent3, agent4],
            tasks=[task1, task2],
            verbose=2,
            process=Process.sequential
        )
        result = crew.kickoff()
        return result


# # Instantiate your crew with a sequential process - TWO AGENTS!
# crew = Crew(
#     agents=[infoSeeker, legaleseBot, guardianAI, sciWritAI],
#     tasks=[research_task, write_task],
#     # llm=ollama_model,
#     verbose=2,
#     # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
#     process=Process.sequential
#     # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
#
# )

# Starting the task execution process with enhanced feedback
# result = crew.kickoff(inputs={'topic': 'LGPD'})

if __name__ == "__main__":
    print("## websearch Crew using toolbox")
    print('-------------------------------')
    # user input a task definition
    search_topic = input("Enter the search topic: ")

    # define a crew object
    crewobj = websearchcrewclass(search_topic)
    # Get your crew to work!
    result = crewobj.run()

    print("###################### result ######################")
    print(result)
