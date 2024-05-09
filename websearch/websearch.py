import os
from crewai import Agent, Task, Crew, Process

from tools import search_tool
from agents import websearchagentsclass
from tasks import websearchtasksclass

from agents import qualityverifyagentclass
from tasks import quality_assurance_tasks_class


# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
# os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

# You can choose to use a local model through Ollama for example. See https://docs.crewai.com/how-to/LLM-Connections/ for more information.

# this is managed by main.py
# # os.environ["OPENAI_API_BASE"] = 'http://host.docker.internal:11434/v1'
# os.environ["OPENAI_API_BASE"] = 'http://llm:11434/v1'
# os.environ["OPENAI_MODEL_NAME"] = 'openhermes'  # Adjust based on available model
# os.environ["OPENAI_API_KEY"] = 'sk-111111111111111111111111111111111111111111111111'

# you can use the serper api , but in this code , we focus on the duckduckgo api
# os.environ["SERPER_API_KEY"] = 'c7a06bdaa06e509b2116cb12ddb60fb773c9693f'
# search_tool = SerperDevTool()


class websearchcrew:
    def __init__(self, search_topic):
        self.search_topic_local1 = search_topic
        self.search_topic_local2 = search_topic

    def run(self):
        # Define your custom agents and tasks here
        agents = websearchagentsclass()
        tasks = websearchtasksclass()

        # Define your custom agents and tasks here
        reseacher_agent_local = agents.researcher_agent()
        writeer_agent_local = agents.writer_agent()

        # Custom tasks include agent name and variables as input
        task1_local = tasks.task_1_name(
            reseacher_agent_local,
            self.search_topic_local1,
            self.search_topic_local2,
        )

        task2_local = tasks.task_2_name(
            writeer_agent_local
        )

        # Define your custom crew here
        crew = Crew(
            agents=[reseacher_agent_local, writeer_agent_local],
            tasks=[task1_local, task2_local],
            verbose=True,
            # verbose=2,  # You can set it to 1 or 2 to different logging levels
        )

        result = crew.kickoff()
        return result


class quality_verify_crew:
    def run(self, search_topic, search_output):
        # Define your custom agents and tasks here
        agents = qualityverifyagentclass()
        tasks = quality_assurance_tasks_class()

        # Define your custom agents and tasks here
        quality_verify_agent_local = agents.quality_verify_agent()

        # Custom tasks include agent name and variables as input
        task1_local = tasks.quality_assurance_task(
            quality_verify_agent_local,
            search_topic,
            search_output
        )

        # Define your custom crew here
        crew = Crew(
            agents=[quality_verify_agent_local],
            tasks=[task1_local],
            verbose=True,
            # verbose=2,  # You can set it to 1 or 2 to different logging levels
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## websearch Crew")
    print('-------------------------------')
    # user input a task definition
    search_topic = input("Enter the search topic: ")

    # define a crew object
    crewobj = websearchcrew(search_topic)
    # Get your crew to work!
    result = crewobj.run()

    qacrewobj = quality_verify_crew()
    qaresult = qacrewobj.run(search_topic, result)

    print("###################### result ######################")
    print(result)
    print("###################### qa result ######################")
    print(qaresult)
