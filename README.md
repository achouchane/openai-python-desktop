# AI Chatbot using OpenAI's GPT-3.5 Turbo

This Python script creates a simple graphical user interface (GUI) / desktop app for interacting with an AI chatbot powered by OpenAI's GPT-3.5 Turbo model or GPT-4. The chatbot engages in a conversation with the user through a text-based interface.

## Functionality

1. **User Input and Display**
   - The GUI allows the user to input text through a text entry field.

2. **Communication with the Chatbot**
   - When the user enters a message and clicks the "Communicate" button, the message is displayed as "You: [user's message]".
   - The message is then sent to the GPT-3.5 Turbo model using the OpenAI API to generate a response.

3. **Chat Display**
   - The conversation between the user and the chatbot is displayed in a text box.
   - The chat history, including both the user's and the assistant's messages, is stored and updated.

4. **Assistant Response**
   - The chatbot's response is displayed as "AI: [AI's response]" in the chat display.

## How to Use

1. **Obtain OpenAI API Key**
   - Replace `"OPENAI_API_KEY"` with your actual OpenAI API key to authenticate and access the GPT-3.5 Turbo model.

2. **Run the Script**
   - Run the Python script, and a GUI window titled "AI Chatbot" will appear.

3. **Interact with the Chatbot**
   - Type your message in the text entry field and press the "Communicate" button.
   - The chatbot will respond, and the conversation will be displayed in the chat display.

## Dependencies

- **OpenAI API**: Requires an API key to access GPT-3.5 Turbo or other model from OpenAI
- **Python Libraries**:
  - `os`: Operating system interface for accessing environment variables.
  - `tkinter`: GUI toolkit for creating the graphical user interface.
  - `openai`: OpenAI Python library for interfacing with the GPT-3.5 Turbo model.

## Notes

- Make sure you have the necessary dependencies installed and configured before running the script.
- Respect OpenAI usage policies and guidelines when utilizing the GPT-3.5 Turbo model.
