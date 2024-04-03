from crewai import Task
from textwrap import dedent


class fileopts_tasks_class:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1):
        return Task(
            description=dedent(
                f"""read out the file from local disk {var1}.
                summary the content of the file. and write one sentence of comment. 
        {self.__tip_section()}""",
            ),
            expected_output=f"A brief summary on the file given.",
            agent=agent,  # infoSeeker_agent,
            # tools=[search_tool],
            output_file='fileops-summary.md'  # Example of output customization
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""Synthesize information from other agents and create a coherent article about the file given.
        {self.__tip_section()}""",
            ),

            expected_output=f"A well-written article about the file given.",
            agent=agent,  # sciWritAI_agent,
            # tools=[search_tool],
            async_execution=False,
            output_file='fileops-search-summary.md'  # Example of output customization
        )
