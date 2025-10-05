import streamlit as st
from src.aurora.main import run_crew # Import the main crew execution function

# --- Page Configuration ---
st.set_page_config(
    page_title="Project Aurora",
    page_icon="🚀",
    layout="centered"
)

# --- UI Elements ---
st.title("🚀 Aurora: Your Agentic Research Companion")
st.markdown("Enter a research topic below and let the AI crew handle the rest.")

# User input
topic = st.text_input("Enter a research topic:", "e.g., The future of lab-grown meat")

# Button to start the research process
if st.button("Start Research"):
    if topic:
        with st.spinner("The Aurora crew is on the case... This may take a few minutes."):
            try:
                # Run the CrewAI process
                final_report = run_crew(topic)
                
                # Display the final report
                st.subheader("Final Research Report")
                st.markdown(final_report)

                # Placeholder for knowledge graph visualization
                st.subheader("Knowledge Graph")
                st.info("Knowledge graph visualization is not yet implemented.")
                # st.image("path/to/generated/graph.png", caption="Key Entities and Relationships")

                # Human-in-the-Loop Feedback Section
                st.subheader("Provide Feedback")
                st.info("Feedback mechanism is not yet connected.")
                col1, col2 = st.columns(2)
                with col1:
                    st.button("👍 Helpful")
                with col2:
                    st.button("👎 Not Helpful")
                st.text_area("Additional comments:")

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a research topic.")