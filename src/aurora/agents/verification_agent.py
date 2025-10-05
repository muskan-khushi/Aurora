from crewai import Agent

def create_verification_agent():
    """
    Creates the Verification Agent, responsible for the final quality check.
    This agent is the "editor" of the crew.
    """
    return Agent(
        role='Meticulous Editor and Final Gatekeeper',
        goal='Perform a final review of the synthesized report, cross-referencing claims against original sources, generating verifiable citations, and mitigating any remaining hallucinations.',
        backstory=(
            "You are the last line of defense for factual accuracy and academic rigor. With an unwavering "
            "commitment to truth, you meticulously examine every statement in the synthesized report. "
            "You trace each claim back to its source document, ensuring perfect faithfulness. You are also "
            "a master of citation, generating perfectly formatted references to provide full verifiability. "
            "Nothing gets past you."
        ),
        tools=[], # This agent cross-references internal data, so no external tools are needed.
        verbose=True,
        allow_delegation=False
    )