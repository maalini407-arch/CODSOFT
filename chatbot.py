import tkinter as tk

def send_message():
    user_input = entry.get().lower()
    
    if user_input == "":
        return

    chat_box.insert(tk.END, "You: " + user_input + "\n")

    # Responses
    if user_input in ["hi", "hello", "hey"]:
        response = "Hello! How can I help you?"
    
    elif "how are you" in user_input:
        response = "I am fine 😊 What about you?"
    
    elif "your name" in user_input:
        response = "I am a rule-based chatbot."
    
    elif "joke" in user_input:
        response = "Why did the computer sleep? Because it was tired 😄"
    
    elif "time" in user_input:
        response = "Sorry, I can't tell time yet ⏰"
    
    elif "thank" in user_input:
        response = "You're welcome 😊"
    
    elif "help" in user_input:
        response = "Try saying: hi, joke, your name, or bye"
    
    elif user_input in ["bye", "exit"]:
        response = "Goodbye! Have a nice day 👋"
    
    else:
        response = "Sorry, I don't understand."

    chat_box.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

# Window
window = tk.Tk()
window.title("Simple Chatbot")
window.geometry("400x500")
window.configure(bg="lightblue")

# Chat area
chat_box = tk.Text(window, height=20, width=50, bg="white")
chat_box.pack(pady=10)

# Input
entry = tk.Entry(window, width=40)
entry.pack(pady=5)

# Button
send_button = tk.Button(window, text="Send", bg="green", fg="white", command=send_message)
send_button.pack()

# Run
window.mainloop()
