import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

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


from langchain.tools import DuckDuckGoSearchRun
from crewai_tools import tool

@tool('duckduckgo')
def search_tool(query: str):
    """Search tool using DuckDuckGo API."""
    print("")
    print(f"=====================================Searching for: {query}")
    searchobj = DuckDuckGoSearchRun()
    # search_result = DuckDuckGoSearchRun(query=query, max_results=5, verbose=True)
    search_result = searchobj.run(query)
    print("=====================================")
    print(f"Search Result: {search_result}")
    return search_result


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
    description="""Conduct a comprehensive analysis of the new ev xiaomi has released in 2024.
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

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
