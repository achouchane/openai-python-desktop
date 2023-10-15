import os
import openai
import tkinter as tk
from tkinter import ttk

openai.api_key = os.getenv("OPENAI_API_KEY")

def communicate():
    message = user_input.get()
    chat_display.insert(tk.END, "You: " + message + "\n")
    user_input.delete(0, tk.END)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant designed to help."},
            *chat_history,
            {"role": "user", "content": message},
        ]
    )

    assistant_response = response.choices[0].message["content"]
    chat_display.insert(tk.END, "AI: ", "bold")
    chat_display.insert(tk.END, assistant_response + "\n")

    chat_history.extend([
        {"role": "user", "content": message},
        {"role": "assistant", "content": assistant_response},
    ])

root = tk.Tk()
root.title("AI Chatbot")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

chat_display = tk.Text(frame, wrap=tk.WORD, width=75, height=20, font=("TkDefaultFont", 12))
chat_display.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))
chat_display.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

user_input = ttk.Entry(frame, width=70, font=("TkDefaultFont", 12))
user_input.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

communicate_button = ttk.Button(frame, text="Communicate", command=communicate)
communicate_button.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

chat_history = []

root.mainloop()

