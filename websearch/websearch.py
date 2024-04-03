import os
from crewai import Agent, Task, Crew, Process

from tools import search_tool
from agents import websearchagentsclass
from tasks import websearchtasksclass

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



# Define your agents with roles and goals
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in technology and data science',
    backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    memory=True,
    # You can pass an optional llm attribute specifying what mode you wanna use.
    # It can be a local model through Ollama / LM Studio or a remote
    # model like OpenAI, Mistral, Antrophic or others (https://docs.crewai.com/how-to/LLM-Connections/)
    #
    # import os
    # os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'
    #
    # OR
    #
    # from langchain_openai import ChatOpenAI
    # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)
)
writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
    verbose=True,
    allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
    description="""Conduct a comprehensive analysis of {search_topic}.
  Identify key trends, breakthrough technologies, and potential industry impacts.""",
    expected_output="Full analysis report in bullet points",
    agent=researcher
)

task2 = Task(
    description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant ev advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
    expected_output="Full blog post of at least 4 paragraphs,approx 500 words.",
    agent=writer
)



# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,  # You can set it to 1 or 2 to different logging levels
)


class websearchcrew:
    def __init__(self, search_topic):
        self.var1 = search_topic
        self.var2 = search_topic

    def run(self):
        # Define your custom agents and tasks here
        agents = websearchagentsclass()
        tasks = websearchtasksclass()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.researcher_agent()
        custom_agent_2 = agents.writer_agent()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.task_1_name(
            custom_agent_1,
            self.var1,
            self.var2,
        )

        custom_task_2 = tasks.task_2_name(
            custom_agent_2,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
            verbose=True,
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

    print("###################### result ######################")
    print(result)
