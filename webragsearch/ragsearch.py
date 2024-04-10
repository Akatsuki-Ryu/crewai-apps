# pip install crewai langchain-community langchain-openai requests duckduckgo-search chromadb

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_core.retrievers import BaseRetriever

from agents import NewsAgentsclass
from tasks import NewsTasksclass

agentsobj = NewsAgentsclass()
news_search_agentobj = agentsobj.news_search_agent
writer_agentobj = agentsobj.writer_agent

tasksobj = NewsTasksclass(news_search_agentobj, writer_agentobj)

news_search_taskobj = tasksobj.create_news_search_task()
writer_taskobj = tasksobj.create_writer_task()

# 4. Creating Crew
news_crew = Crew(
    agents=[news_search_agentobj, writer_agentobj],
    tasks=[news_search_taskobj, writer_taskobj],
    process=Process.sequential,
    # manager_llm=llm
)

# Execute the crew to see RAG in action
result = news_crew.kickoff()
print(result)
