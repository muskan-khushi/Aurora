from dotenv import load_dotenv
from crewai import Crew, Process, Task

# Import your agent creation functions
from aurora.agents.retrieval_agent import create_retrieval_agent
from aurora.agents.critique_agent import create_critique_agent
from aurora.agents.synthesis_agent import create_synthesis_agent
from aurora.agents.verification_agent import create_verification_agent

# Load environment variables
load_dotenv()

# --- 1. Instantiate Agents ---
retrieval_agent = create_retrieval_agent()
critique_agent = create_critique_agent()
synthesis_agent = create_synthesis_agent()
verification_agent = create_verification_agent()

# --- 2. Define Tasks ---
# Each task has a specific agent assigned to it and a clear description of what's expected.

retrieval_task = Task(
    description="Conduct a thorough research on the topic: '{topic}'. Gather relevant academic papers and recent news articles to form a comprehensive knowledge base.",
    expected_output="A collection of relevant text snippets with source metadata, stored and ready for analysis.",
    agent=retrieval_agent
)

critique_task = Task(
    description="Critically evaluate the collection of research materials. Identify any conflicting information, assess the credibility of sources, and flag potential biases. Note any gaps in the information.",
    expected_output="An annotated set of information with quality scores, flags for contradictions, and suggestions for areas needing more research. This curated data is the single source of truth for the next step.",
    agent=critique_agent,
    context=[retrieval_task] # This task depends on the output of the retrieval_task
)

synthesis_task = Task(
    description="Synthesize the curated and critiqued information into a coherent, well-structured, and insightful narrative. The report should identify key themes, connections, and potential implications.",
    expected_output="A comprehensive draft of the final report, written in a clear, narrative style. It should be well-organized and present the information in a way that uncovers deeper insights.",
    agent=synthesis_agent,
    context=[critique_task] # This task depends on the output of the critique_task
)

verification_task = Task(
    description="Perform a final verification of the synthesized report. Cross-reference every key claim against the original source documents to ensure factual accuracy. Generate APA-formatted citations for all sources used.",
    expected_output="The final, polished report with a high degree of factual grounding, free of hallucinations, and complete with verifiable citations in APA format.",
    agent=verification_agent,
    context=[synthesis_task] # This task depends on the output of the synthesis_task
)

# --- 3. Assemble the Crew ---
# The Crew object brings the agents and tasks together.
# The process is sequential, meaning tasks will be executed one after another.

research_crew = Crew(
    agents=[retrieval_agent, critique_agent, synthesis_agent, verification_agent],
    tasks=[retrieval_task, critique_task, synthesis_task, verification_task],
    process=Process.sequential,
    verbose=2 # Verbose level 2 for detailed agent thought processes
)

# --- 4. Define a function to run the crew ---
def run_crew(topic: str):
    """Kicks off the research crew with a specific topic."""
    result = research_crew.kickoff(inputs={'topic': topic})
    return result

# --- 5. Run the crew for testing if the script is executed directly ---
if __name__ == "__main__":
    topic = "The impact of AI on scientific research"
    print(f"🚀 Starting the Aurora research crew for the topic: '{topic}'")
    final_report = run_crew(topic)
    print("\n\n✅ --- Final Research Report --- ✅")
    print(final_report)