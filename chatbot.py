print("Welcome to the chatbot")

def chatbot():
    while True:
        user_input = input("You: ")

        if user_input == "":
            print("Bot: Please say something.")
        elif user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot:", user_input)

chatbot()



