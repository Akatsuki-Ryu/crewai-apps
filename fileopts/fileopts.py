import os
from crewai import Agent, Task, Crew, Process

from agents import fileops_agents_class
from tasks import fileopts_tasks_class


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


class fileops_crew:
    def __init__(self, filename):
        self.filename_local = filename
        # self.search_topic_local2 = search_topic

    def run(self):
        # Define your custom agents and tasks here
        agents = fileops_agents_class()
        tasks = fileopts_tasks_class()

        # Define your custom agents and tasks here
        agent1 = agents.info_reading_agent()
        agent2 = agents.info_summary_agent()
        agent3 = agents.file_writing_agent()

        # Custom tasks include agent name and variables as input
        task1_local = tasks.task_1_name(
            agent2,
            self.filename_local
        )

        # task2_local = tasks.task_1_name(
        #     agent2,
        #     self.filename_local
        # )

        # Define your custom crew here
        crew = Crew(
            agents=[agent1, agent2],
            tasks=[task1_local],
            verbose=True,
            # verbose=2,  # You can set it to 1 or 2 to different logging levels
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## file ops Crew")
    print('-------------------------------')
    # user input a task definition
    search_topic = input("Enter the file name: ")

    # define a crew object
    crewobj = fileops_crew(search_topic)
    # Get your crew to work!
    result = crewobj.run()

    print("###################### result ######################")
    print(result)
