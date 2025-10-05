import os
import semanticscholar as s2
from crewai_tools import Tool
from dotenv import load_dotenv

load_dotenv()

def _search_semantic_scholar(query: str) -> str:
    """Internal function to search Semantic Scholar."""
    try:
        s2.api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
        print(f"INFO: Searching Semantic Scholar for: '{query}'")
        results = s2.search_paper(query, limit=5)

        if not results:
            return "No academic papers found for this query."

        formatted_results = []
        for item in results:
            abstract = item.abstract if item.abstract else "No abstract available."
            formatted_results.append(
                f"Title: {item.title}\n"
                f"Abstract: {abstract}\n"
                f"URL: {item.url}\n---"
            )
        return "\n".join(formatted_results)
    except Exception as e:
        return f"An error occurred during Semantic Scholar search: {e}"

search_semantic_scholar_tool = Tool(
    name="Semantic Scholar Search",
    description="Searches the Semantic Scholar database for academic papers. Returns top 5 results with title, abstract, and URL.",
    func=_search_semantic_scholar
)