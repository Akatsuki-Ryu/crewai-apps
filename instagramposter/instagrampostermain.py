from dotenv import load_dotenv

load_dotenv()

from textwrap import dedent
from crewai import Agent, Crew

from tasks import MarketingAnalysisTasks, quality_assurance_tasks_class
from agents import MarketingAnalysisAgents, QualityControlAgentsClass


class copy_crew:
    # def __init__(self):
    #     self.tasks = MarketingAnalysisTasks()
    #     self.agents = MarketingAnalysisAgents()

    def run(self, product_website, product_details):
        taskspbj = MarketingAnalysisTasks()
        agentsobj = MarketingAnalysisAgents()

        print("## Welcome to the marketing Crew")
        print('-------------------------------')
        # product_website = input("What is the product website you want a marketing strategy for?\n")
        # product_details = input("Any extra details about the product and or the instagram post you want?\n")

        # Create Agents
        product_competitor_agent = agentsobj.product_competitor_agent()
        strategy_planner_agent = agentsobj.strategy_planner_agent()
        creative_agent = agentsobj.creative_content_creator_agent()
        # Create Tasks
        website_analysis = taskspbj.product_analysis(product_competitor_agent, product_website, product_details)
        market_analysis = taskspbj.competitor_analysis(product_competitor_agent, product_website, product_details)
        campaign_development = taskspbj.campaign_development(strategy_planner_agent, product_website, product_details)
        write_copy = taskspbj.instagram_ad_copy(creative_agent)

        # Create Crew responsible for Copy
        copy_crew = Crew(
            agents=[
                product_competitor_agent,
                strategy_planner_agent,
                creative_agent
            ],
            tasks=[
                website_analysis,
                market_analysis,
                campaign_development,
                write_copy
            ],
            verbose=True
        )

        ad_copy = copy_crew.kickoff()
        return ad_copy


class image_crew:
    # def __init__(self):
    #     self.tasks = MarketingAnalysisTasks()
    #     self.agents = MarketingAnalysisAgents()

    def run(self, ad_copy, product_website, product_details):
        taskspbj = MarketingAnalysisTasks()
        agentsobj = MarketingAnalysisAgents()

        # Create Crew responsible for Image
        senior_photographer = agentsobj.senior_photographer_agent()
        chief_creative_diretor = agentsobj.chief_creative_diretor_agent()
        # Create Tasks for Image
        take_photo = taskspbj.take_photograph_task(senior_photographer, ad_copy, product_website, product_details)
        approve_photo = taskspbj.review_photo(chief_creative_diretor, product_website, product_details)

        image_crew = Crew(
            agents=[
                senior_photographer,
                chief_creative_diretor
            ],
            tasks=[
                take_photo,
                approve_photo
            ],
            verbose=True
        )

        image = image_crew.kickoff()
        return image


class QualityAssuranceCrew:
    def __init__(self):
        self.tasks = quality_assurance_tasks_class()
        self.agents = QualityControlAgentsClass()

    def run(self, product_website, product_details, task_output):
        # Create Agent
        quality_control_agent = self.agents.quality_control_agent()

        # Create Task
        quality_assurance_task = self.tasks.quality_assurance(quality_control_agent, product_website, product_details,
                                                              task_output)

        # Create Crew responsible for Quality Assurance
        quality_assurance_crew = Crew(
            agents=[quality_control_agent],
            tasks=[quality_assurance_task],
            verbose=True
        )

        # Run the quality assurance task
        qa_report = quality_assurance_crew.kickoff()
        return qa_report


if __name__ == "__main__":
    print("## instagramposter Crew")
    print('-------------------------------')

    product_website = input("What is the product website you want a marketing strategy for?\n")
    product_details = input("Any extra details about the product and or the instagram post you want?\n")

    copy_crewobj = copy_crew()
    ad_copy = copy_crewobj.run(product_website, product_details)

    qualityassuranceobj_ad_copy = QualityAssuranceCrew()
    qualityassurance_ad_copy = qualityassuranceobj_ad_copy.run(product_website, product_details, ad_copy)

    image_crewobj = image_crew()
    image = image_crewobj.run(ad_copy, product_website, product_details)

    qualityassuranceobj_image = QualityAssuranceCrew()
    qualityassurance_image = qualityassuranceobj_image.run(product_website, product_details, image)

    # Print results
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print("Your post copy:")
    print(ad_copy)
    print("'\n\nYour midjourney description:")
    print(image)
    print("\n\nYour quality assurance report for post:")
    print(qualityassurance_ad_copy)
    print("\n\nYour quality assurance report for image:")
    print(qualityassurance_image)
    print("\n\n########################")
