from crewai import Task
from textwrap import dedent


class websearchtasksclass:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
       Conduct a comprehensive analysis of {var1}.
  Identify key trends, breakthrough technologies, and potential industry impacts.
            {self.__tip_section()}
        """,
            ),
            expected_output="Full analysis report in bullet points",
            agent=agent,
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
           Using the insights provided, develop an engaging blog
  post that highlights the most significant ev advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.                                  
            {self.__tip_section()}
        """
            ),
            expected_output="Full blog post of at least 4 paragraphs,approx 500 words.",
            agent=agent,
        )


class quality_assurance_tasks_class:
    def quality_assurance_task(self, agent, search_topic, search_output):
        return Task(
            description=dedent(
                f"""
                Verify the accuracy and quality of the content for the search output.
                Ensure that the search topic aligns with the search output.
                search topic:{search_topic}.
                search output:{search_output}.
            """
            ),
            expected_output="Quality assurance report, if the search topic does not match the search output, provide feedback.",
            agent=agent,
            # task_output=task_output
        )
