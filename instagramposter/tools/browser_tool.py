import json

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html


from crewai_tools import ScrapeWebsiteTool


class BrowserTools():

    @tool("Scrape website content")
    def scrape_and_summarize_website(websiteurl):
        """Useful to scrape and summarize a website content, just pass a string with
        only the full url, no need for a final slash `/`, eg: https://google.com or https://clearbit.com/about-us"""
        # url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        # serviceurl = f"http://localhost:3000/content" # running browserless locally
        serviceurl = f"http://browserless_chromium:3000/content" # running browserless through docker network
        print("\n===================target website ====================")
        print(websiteurl)
        payload = json.dumps({"url": websiteurl})
        headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
        response = requests.request("POST", serviceurl, headers=headers, data=payload)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
        print("\n===================scrapted content =====================")
        print(content)
        summaries = []
        for chunk in content:
            agent = Agent(
                role='Principal Researcher',
                goal=
                'Do amazing researches and summaries based on the content you are working with',
                backstory=
                "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
                # llm=Ollama(model=os.environ['MODEL']),
                allow_delegation=False)
            task = Task(
                agent=agent,
                description=
                f'Analyze and make a LONG summary the content bellow, make sure to include the ALL relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}',
                expected_output='A long summary of the content provided'
            )
            summary = task.execute()
            summaries.append(summary)
            content = "\n\n".join(summaries)
        return f'\nScrapped Content: {content}\n'
