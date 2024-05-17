"""
# ARCHBOT APP 

You can access app on <a href="https://archie.streamlit.app"> archat</a>

This Streamlit application, named "ArchieChat," serves as a conversational interface powered by the `Hugging Face chatbot API` and `OPEN AI API`. The application enables users to interact with the chatbot by providing text-based input and receiving responses in real-time. The primary functionalities of the application are:

1. User Authentication: Users can provide their Hugging Face login credentials (email and password) via the sidebar. If the credentials are already provided or stored in a .env file, the application retrieves them automatically.

2. Chat Interface: The main section of the application features a chat interface where users can input messages and receive responses from the chatbot. The chat interface displays messages exchanged between the user and the assistant, maintaining a conversational flow.

3. Message Handling: The application manages user-provided messages and assistant responses using the st.session_state.messages variable. Messages are stored in this variable to maintain continuity in the conversation.

4. Generating Responses: The application includes a function called generate_response, which is responsible for generating responses from the Hugging Face chatbot API. It constructs a prompt by incorporating previous messages exchanged between the user and the assistant, ensuring contextual relevance.

5. User Input Handling: Users can input messages using the st.chat_input function, allowing them to interact with the chatbot seamlessly. The application dynamically updates the chat interface with user messages and corresponding assistant responses.

6. Response Generation: When a user provides input, the application triggers the generate_response function to generate a response from the chatbot. It then displays the response in the chat interface, maintaining the conversational flow.

"""

# OpenAI API version

https://github.com/Archly2022/AI-Chatbot/assets/97497497/e2488618-3567-490a-8e24-489f8188c5b9


<img width="1071" alt="archie" src="https://github.com/Archly2022/AI-Chatbot/assets/97497497/85d999de-7f8b-44d5-be24-7b3134393b99">






# HUGGING CHAT Version

<img width="1085" alt="arcgchat" src="https://github.com/Archly2022/AI-Chatbot/assets/97497497/a6eb6a22-55fc-427b-976e-8bf61cf438a2">



