from crewai import Agent, Task, Crew, Process
from agents import news_search_agent, writer_agent
from tools import search_tool, SearchNewsDB, GetNews

# 3. Creating Tasks
news_search_task = Task(
    description='Search for AI 2024 and create key points for each news.',
    agent=news_search_agent,
    expected_output='Key points for each news article from the latest news.',
    tools=[SearchNewsDB().news]
)

writer_task = Task(
    description=f"""
    Go step by step.
    Step 1: Identify all the topics received.
    Step 2: Use the Get News Tool to verify the each topic by going through one by one.
    Step 3: Use the Search tool to search for information on each topic one by one. 
    Step 4: Go through every topic and write an in-depth summary of the information retrieved.
    Don't skip any topic.
    """,
    agent=writer_agent,
    context=[news_search_task],
    expected_output='Summarised information for every topic.',
    tools=[GetNews().news, search_tool]
)
