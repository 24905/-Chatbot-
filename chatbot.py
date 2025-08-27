def chatbot():
    print("Chatbot: Hello! I'm your friendly bot")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How’s your day going?")
        elif user_input in ["i am fine", "good", "great", "awesome"]:
            print("Chatbot: That’s nice to hear! 😊")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm doing great, thanks for asking!")
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I'm just a simple chatbot created to talk with you.")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        else:
            print("Chatbot: Hmm... I don’t know how to reply to that yet.")

chatbot()
