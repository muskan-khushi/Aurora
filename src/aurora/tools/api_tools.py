import os
import semanticscholar as s2
from crewai_tools import tool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SearchTools:
    @tool("Semantic Scholar Search")
    def search_semantic_scholar(query: str) -> str:
        """
        Searches the Semantic Scholar database for academic papers related to the query.
        Returns a formatted string of the top 5 results, including title, abstract, and URL.
        """
        try:
            # Set the API key for the semanticscholar library, if it exists in the environment
            s2.api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

            print(f"INFO: Searching Semantic Scholar for: '{query}'")
            results = s2.search_paper(query, limit=5)

            if not results:
                return "No academic papers found for this query."

            formatted_results = []
            for item in results:
                # Ensure abstract is not None and provide a fallback
                abstract = item.abstract if item.abstract else "No abstract available."
                formatted_results.append(
                    f"Title: {item.title}\n"
                    f"Abstract: {abstract}\n"
                    f"URL: {item.url}\n---"
                )
            return "\n".join(formatted_results)

        except Exception as e:
            return f"An error occurred during Semantic Scholar search: {e}"