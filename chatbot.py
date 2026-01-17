def chatbot():
    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello!",
        "how are you": "I am fine, thank you!",
        "what is your name": "I am a simple Python Chatbot.",
        "bye": "Goodbye! Have a nice day."
    }

    print("Chatbot Started (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()