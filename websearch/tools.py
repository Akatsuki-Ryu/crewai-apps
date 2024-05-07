from crewai_tools import SerperDevTool

from langchain_community.tools import DuckDuckGoSearchRun

from crewai_tools import tool


@tool('duckduckgo')
def search_tool(query: str):
    """Search tool using DuckDuckGo API."""
    print("")
    print(f"=====================================Searching for: {query}")
    searchobj = DuckDuckGoSearchRun()
    # search_result = DuckDuckGoSearchRun(query=query, max_results=5, verbose=True)
    search_result = searchobj.run(query)
    print("=====================================")
    print(f"Search Result: {search_result}")
    return search_result

