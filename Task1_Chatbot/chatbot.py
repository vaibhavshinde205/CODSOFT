import random
from datetime import datetime

def load_jokes():
    try:
        with open("jokes.txt", "r") as file:
            jokes = file.readlines()
        return [joke.strip() for joke in jokes]
    except:
        return ["Sorry, I don't have any jokes right now!"]

def load_motivation():
    try:
        with open("motivation.txt", "r") as file:
            quotes = file.readlines()
        return [quote.strip() for quote in quotes]
    except:
        return ["Keep going, you're doing great!"]


print("----- Simple AI Chatbot -----")
print("Type 'exit' anytime to stop\n")

name = input("Chatbot: Hello! What is your name?\nYou: ")
print(f"Chatbot: Nice to meet you, {name}!")

jokes_list = load_jokes()
motivation_list = load_motivation()

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print(f"Chatbot: Goodbye {name}! Have a nice day!")
        break

    greetings = ["hi", "hello", "hey"]
    if user_input in greetings:
        print("Chatbot:", random.choice([
            "Hello there!",
            "Hi! How can I help you?",
            "Hey! What's up?"
        ]))

    elif "how are you" in user_input:
        print("Chatbot: I'm just a program, but I'm doing great!")

    elif "your name" in user_input:
        print("Chatbot: I am your friendly rule-based chatbot.")

    elif "time" in user_input:
        print("Chatbot: Current time is", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user_input:
        print("Chatbot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif "add" in user_input:
        print("Chatbot: Enter two numbers to add.")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Chatbot: The sum is:", a + b)
   
    elif "subtract" in user_input:
        print("Chatbot: Enter two numbers to subtract.")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Chatbot: The subtraction is:", a - b)
    
    elif "multiply" in user_input:
        print("Chatbot: Enter two numbers to multiply.")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Chatbot: The multiplication is:", a * b)

    elif "divide" in user_input:
        print("Chatbot: Enter two numbers to division.")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Chatbot: The division is:", a / b)

    elif "joke" in user_input:
        print("Chatbot:", random.choice(jokes_list))

    elif "motivate" in user_input or "motivation" in user_input:
        print("Chatbot:", random.choice(motivation_list))

    elif "help" in user_input:
        print("Chatbot: Here are some things you can ask me:")
        print("- Say hello")
        print("- Ask my name")
        print("- Ask time or date")
        print("- Ask me to perform basic maths")
        print("- Type exit to quit")
        print("- Ask me to tell a joke")
        print("- Ask for motivation")


    else:
        print("Chatbot: Sorry, I don't understand that. Type 'help' to see options.")
