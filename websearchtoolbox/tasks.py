from crewai import Task
from agents import websearchtoolboxagentsclass
from textwrap import dedent


class websearchtoolboxtasksclass:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1):
        return Task(
            description=dedent(
                f"""Identify the next big trend in {var1}.
                Focus on identifying pros and cons and the overall narrative.
                Your final report should clearly articulate the key points
                its market opportunities, and potential risks.
        {self.__tip_section()}""",
            ),
            expected_output=f"A comprehensive long article on the latest {var1}.",
            agent=agent,  # infoSeeker_agent,
            # tools=[search_tool],
        )

    def task_2_name(self, agent, var1):
        return Task(
            description=dedent(
                f"""Synthesize information from other agents and create a coherent article on {var1}.
        {self.__tip_section()}""",
            ),

            expected_output=f"A well-written scientific article about {var1}.",
            agent=agent,  # sciWritAI_agent,
            # tools=[search_tool],
            async_execution=False,
            output_file='search-summary.md'  # Example of output customization
        )
