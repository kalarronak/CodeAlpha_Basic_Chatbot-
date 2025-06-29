
import tkinter as tk
from tkinter import scrolledtext
from datetime import date, datetime
import webbrowser  # For Google search

# Function to generate chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you?"

    elif user_input == "how are you":
        return "I'm doing well, thank you! How about you?"

    elif user_input in ["i'm fine", "i am good", "i'm doing well"]:
        return "That's great to hear!"

    elif user_input in ["what's your name", "what is your name"]:
        return "I'm a simple chatbot created to help you."

    elif user_input == "who created you":
        return "I was created by a Python programmer as a fun project."

    elif user_input == "tell me a joke":
        return "Why do Java developers wear glasses? Because they don’t C#! 😄"

    elif user_input == "what's the date today":
        today = date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}"

    elif user_input == "what's the time":
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}"

    elif user_input == "what is python":
        return "Python is a powerful, easy-to-learn programming language used for many types of applications."

    elif user_input == "can you help me learn python":
        return "Of course! Start with variables: try typing print('Hello, Python!')"

    elif user_input == "what can you do":
        return "I can answer simple questions, tell jokes, help with Python, and even search Google for you!"

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif "debug my code" in user_input:
        return "Sure! Paste your code and I’ll try to help."

    elif "google" in user_input or "search" in user_input:
        try:
            query = user_input.replace("google", "").replace("search", "").strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                return f"Searching Google for: {query}"
            else:
                return "Please specify what to search for."
        except:
            return "Failed to open browser. Please try again."

    elif "bye" in user_input or "byy" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Try asking something else!"

# Function to handle user input
# Handles both button click and Enter key
def send_message(event=None):  
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

# Set up the main window
window = tk.Tk()
window.title("Chatbot with Google Search")
window.geometry("500x450")

# Chat display area
chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=55, height=20, state='normal')
chat_window.pack(pady=10)

# Insert welcome message
chat_window.insert(tk.END, "Bot: Hello!\n")
chat_window.insert(tk.END, "Bot: Welcome to the Simpleand smart Chatbot!\n")
chat_window.insert(tk.END, "Bot: Ask me anything, or search Google.Type Search...\n\n")


# Input field
entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=5)
entry.bind("<Return>", send_message)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

# Run the GUI
window.mainloop()
