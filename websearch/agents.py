from crewai import Agent, Task, Crew, Process
from tools import search_tool

# Define your agents with roles and goals
class websearchagentsclass:
    # def __init__(self):
    # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    # self.Ollama = Ollama(model="openhermes")

    def researcher_agent(self):
        return Agent(
            role='Senior Research Analyst',
            goal='Uncover cutting-edge developments in technology and data science',
            backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            memory=True,
            # llm=self.OpenAIGPT35,
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

    def writer_agent(self):
        return Agent(
            role='Tech Content Strategist',
            goal='Craft compelling content on tech advancements',
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True
            # tools=[tool_1, tool_2],
            # llm=self.OpenAIGPT35,
        )

class qualityverifyagentclass:
    def quality_verify_agent(self):
        return Agent(
            role='Quality Assurance Specialist',
            goal='Ensure the accuracy and quality of the content',
            backstory="""You are a meticulous Quality Assurance Specialist with an eye for detail.
  Your role is to verify the accuracy of research topic and the output result.""",
            verbose=True,
            allow_delegation=False
        )