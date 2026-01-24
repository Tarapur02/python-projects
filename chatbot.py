

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 😊 How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😄"

    elif "your name" in user_input:
        return "I'm a simple Python Chatbot 🤖"

    elif "help" in user_input:
        return "Sure! You can ask me about Python, projects, or general questions."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day 👋"

    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)
    print("🤖 Chatbot:", response)

    if "bye" in user_message.lower() or "exit" in user_message.lower():
        break
