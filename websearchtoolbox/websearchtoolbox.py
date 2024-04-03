import os
from crewai import Agent, Task, Crew, Process

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
    # llm=ollama_model,
    verbose=2,
    # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
    process=Process.sequential
    # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.

)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'LGPD'})
