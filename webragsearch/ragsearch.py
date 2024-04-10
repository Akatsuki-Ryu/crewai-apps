# pip install crewai langchain-community langchain-openai requests duckduckgo-search chromadb

from crewai import Agent, Task, Crew, Process

from tools import SearchNewsDB, GetNews, search_tool
from agents import news_search_agent, writer_agent
from tasks import news_search_task, writer_task


# 4. Creating Crew
news_crew = Crew(
    agents=[news_search_agent, writer_agent],
    tasks=[news_search_task, writer_task],
    process=Process.sequential,
    # manager_llm=llm
)

# Execute the crew to see RAG in action
result = news_crew.kickoff()
print(result)
