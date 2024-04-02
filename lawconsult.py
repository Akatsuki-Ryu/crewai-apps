import os
from crewai import Agent, Task, Crew, Process

from langchain_community.llms import Ollama

from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Instantiate tools
# docs_tool = DirectoryReadTool(directory='./blog-posts')
# file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# this is managed by the main.py
model_name = os.getenv("OPENAI_MODEL_NAME")
# base_url = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
base_url = os.getenv("OPENAI_API_BASE")

os.environ["SERPER_API_KEY"] = 'c7a06bdaa06e509b2116cb12ddb60fb773c9693f'

# Initialize the Ollama model with the specified model and base URL
ollama_model = Ollama(model=model_name, base_url=base_url)

### OPENAI
# os.environ["OPENAI_API_KEY"] = "Your Key"
# export OPENAI_API_KEY=sk-blablabla # on Linux/Mac

infoSeeker = Agent(
    role="Researcher Agent",
    goal="Gather relevant information about GDPR",
    backstory="You was born in the digital libraries of academia."
              "Its creators, a team of data scientists and researchers,"
              "designed it to be an insatiable seeker of knowledge.",
    verbose=True,
    memory=True,
    allow_delegation=True,
    tools=[search_tool, web_rag_tool],
    llm=ollama_model
)
legaleseBot = Agent(
    role="Legal Analyst Agent",
    goal="Interpret GDPR regulations and legal implications",
    backstory="You emerged from the depths of legal archives."
              "Its neural circuits were meticulously trained on centuries of jurisprudence."
              "Its purpose: to decipher complex regulations and translate them into plain language.",
    verbose=True,
    memory=True,
    allow_delegation=False,
    tools=[search_tool, web_rag_tool],
    llm=ollama_model
)
guardianAI = Agent(
    role="Ethics and Privacy Agent",
    goal="Address ethical considerations and privacy implications",
    backstory="You was forged in the fires of ethical debates. "
              "Its creators, a team of philosophers and privacy advocates, endowed it with a moral compass. "
              "Mission: to protect individual rights and navigate the treacherous waters of data ethics.",
    verbose=True,
    memory=True,
    allow_delegation=False,
    tools=[search_tool, web_rag_tool],
    llm=ollama_model
)
sciWritAI = Agent(
    role="Content Generator Agent",
    goal="Create a coherent scientific article",
    backstory="You are the intersection of creativity and logic. "
              "Its neural pathways were fine-tuned by poets and scientists alike. Its purpose: "
              "to weave words into a tapestry of knowledge, bridging the gap between data and understanding.",
    verbose=True,
    memory=True,
    allow_delegation=False,
    tools=[search_tool, web_rag_tool],
    llm=ollama_model
)

research_task = Task(
    description=
    """Identify the next big trend in {topic}.
    Focus on identifying pros and cons and the overall narrative.
    Your final report should clearly articulate the key points
    its market opportunities, and potential risks.""",
    expected_output="A comprehensive long article on the latest {topic}.",
    # tools=[search_tool],
    agent=infoSeeker,
)

# Writing task with language model configuration
write_task = Task(
    # description=(
    #   "Compose an insightful article on {topic}."
    #   "Focus on the latest trends and how it's impacting the industry."
    #   "This article should be easy to understand, engaging, and positive."
    # ),
    # expected_output='A article on {topic} advancements formatted as markdown.',
    description="Synthesize information from other agents and create a coherent article on {topic}.",
    expected_output="A well-written scientific article about {topic}.",
    # tools=[search_tool],
    agent=sciWritAI,
    async_execution=False,
    output_file='artcle.md'  # Example of output customization
)

# Instantiate your crew with a sequential process - TWO AGENTS!
crew = Crew(
    agents=[infoSeeker, legaleseBot, guardianAI, sciWritAI],
    tasks=[research_task, write_task],
    llm=ollama_model,
    verbose=2,
    # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
    process=Process.sequential
    # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.

)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'LGPD'})
