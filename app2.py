import streamlit as st
from assistant import OpenAssist  # open ai assistant

@st.cache
def get_api_call():
    manager = OpenAssist()
    return manager

def main():
    manager = OpenAssist()

    st.title("Archie AI Assistant")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Get previous response from the assistant
    previous_response = manager.get_previous_response()
    st.text("Archie")
    st.write(previous_response, value=previous_response, height=100, max_chars=None, key='previous_response')
    st.markdown("---")

    # Prompt message for the user input
    prompt_message = "You are a helpful assistant.\n"
    for message in st.session_state.messages:
        if message["role"] == "user":
            prompt_message += f"User: {message['content']}\n\n"
        else:
            prompt_message += f"Assistant: {message['content']}\n\n"
            
    # Get user input
    user_input = st.text_area("Ask anything...", height=100, max_chars=None)

    if st.button("Run Assistant"):
        # Create the message with the updated prompt message
        manager.create_message(prompt_message + user_input)
        
        # Run the assistant
        run = manager.run_assistant()
        st.cache_data()
        manager.wait_for_run_completion(run.id)

        # Display the summary
        st.write(manager.get_summary())

if __name__ == "__main__":
    main()
