# A Simple Chatbot that responds to user input with predefined responses.
import tkinter as tk
from tkinter import scrolledtext
def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a program, but thanks for asking! How can I assist you?"
    elif 'your name' in user_input:
        return "I'm a simple chatbot created to assist you."
    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a great day!"
    elif 'help' in user_input:
        return "Sure! I can help you with general questions. What do you need assistance with?"
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome! If you have any more questions, feel free to ask."
    elif 'what is your purpose' in user_input:
        return "My purpose is to assist you with your queries and provide information."
    elif 'tell me a joke' in user_input:
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif 'what is your favorite color' in user_input:
        return "I don't have a favorite color, but I think blue is nice!"
    elif 'what is your favorite food' in user_input:
        return "I don't eat, but I hear pizza is quite popular!"
    elif 'who are you?' in user_input:
        return "I'm a chatbot created to assist you with your questions. How can I help you today?"
    elif 'what can you do?' in user_input:
        return "I can answer questions, tell jokes, and provide information. Just ask me anything!"
    elif 'tell me a story' in user_input:
        return "Once upon a time, in a land far away, there lived a wise old owl who knew all the secrets of the forest."
    elif 'what is the weather like' in user_input:
        return "I don't have real-time data, but you can check a weather website or app for the latest updates."
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"



def send_message():
    user_input = entry.get()
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_area.insert(tk.END, "Chatbot: " + response + "\n")
    entry.delete(0, tk.END)

#GUI setup
window = tk.Tk()
window.title("Simple Chatbot")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state='normal')
chat_area.pack(padx=10, pady=10)

entry = tk.Entry(window, width=50)
entry.pack(padx=10, pady=5)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

#Enter key to send message
window.bind('<Return>', lambda event: send_message())  

#Close button
close_button = tk.Button(window, text="Close", command=window.destroy)
close_button.pack(pady=5)

window.mainloop()


