import streamlit as st
import logging
from io import StringIO
import sys
from news_agent.main import customer_interaction_agent
# Configure logging to capture agent output
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)


# Initialize the agent
@st.cache_resource
def get_agent():
    return customer_interaction_agent()

def main():
    st.title("📰 News Curator Assistant")
    st.markdown("*Your intelligent assistant for fetches articles from various aggregators, filters them by relevance, and summarizes each into a clean, easy-to-read digest*")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "agent" not in st.session_state:
        st.session_state.agent = get_agent()

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("How can I help you with your case today?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Capture the agent's output
                    old_stdout = sys.stdout
                    sys.stdout = captured_output = StringIO()

                    # Call the agent
                    response = st.session_state.agent(prompt)

                    # Restore stdout
                    sys.stdout = old_stdout

                    # Get the captured output
                    agent_output = captured_output.getvalue()

                    # Display the response
                    if agent_output.strip():
                        st.markdown(agent_output)
                        response_content = agent_output
                    else:
                        st.markdown("I'm processing your request...")
                        response_content = "I'm processing your request..."

                except Exception as e:
                    error_msg = f"An error occurred: {str(e)}"
                    st.error(error_msg)
                    response_content = error_msg

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_content})

    # Sidebar with helpful information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    The **news-curator-agent** fetches articles from various aggregators, filters them by relevance, and summarizes each into a clean, easy-to-read digest.

    **What I can help with:**
    - Curating top news from multiple sources
    - Filtering articles by topics or keywords
    - Summarizing complex stories clearly
    - Delivering concise, relevant news digests

    **Tips:**
    - Ask for news on specific topics (e.g., AI, climate, finance)
    - Specify date ranges or sources if needed
    - Use follow-up prompts for deeper summaries
    """)

    st.header("🔧 Actions")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    if st.button("Reset Agent"):
        if "agent" in st.session_state:
            del st.session_state.agent
        st.session_state.agent = get_agent()
        st.success("Agent reset successfully!")


if __name__ == "__main__":
    main()