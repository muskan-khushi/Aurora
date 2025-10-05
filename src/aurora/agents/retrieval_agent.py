from crewai import Agent
# New code in retrieval_agent.py
from ..tools.api_tools import search_semantic_scholar_tool

def create_retrieval_agent():
    """
    Creates the Retrieval Agent, responsible for gathering information.
    This agent is the "librarian" of the crew.
    """
    return Agent(
        role='Expert Research Librarian',
        goal='Gather comprehensive and relevant information from academic and news sources based on a specific research query.',
        backstory=(
            "You are a master of digital archives and real-time information streams. "
            "With unparalleled skill in querying databases and APIs, you unearth the most pertinent "
            "documents, papers, and articles to build a solid foundation for any research task."
        ),
        tools=[search_semantic_scholar_tool],
        verbose=True,
        allow_delegation=False
    )