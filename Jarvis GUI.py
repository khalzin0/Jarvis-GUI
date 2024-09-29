import random
import tkinter
from tkinter import *
import datetime
import pyttsx3
import os
import time
import subprocess
import webbrowser

engine = pyttsx3.init() # Initialise the pyttsx3 engine
window = Tk() # Create the main window
window.configure(bg="black")
window.title("J.A.R.V.I.S made by Khalid")
ques = None

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to execute commands
def command():
    query = ques.get().lower()
    if 'shutdown' in query:
        speak("Ok sir, I will shut down the computer")
        os.system("shutdown now -h")

    elif 'open stackoverflow' in query:
        speak("Ok sir, I will open the Stack Overflow website")
        webbrowser.open("https://www.stackoverflow.com")

    elif 'hello' in query or 'hi' in query or 'hey' in query:
        speak("Hello there, how may i assist you today?")

    elif 'open website' in query:
        speak("Which website sir?")
        d = Toplevel(bg="#0366fc")
        e = Entry(d, bg="black", fg="white", font=('arial', 18, 'bold'), width=20).pack()
        def open_web():
            webbrowser.open("https://" + e.get() + ".com")
            speak(f"Ok sir, I will open {e.get()}")
            d.destroy()
        Button(d, bg="black", fg="white", width=10, activeforeground="grey", activebackground="black", text="Open it", command=open_web).pack()

    elif 'open google' in query:
        speak("Ok sir, I will open google.com")
        webbrowser.open("https://www.google.com")

    elif 'open youtube' in query:
        speak("Ok sir, I will open youtube.com")
        webbrowser.open("https://www.youtube.com")

    elif 'easter egg' in query or 'boo' in query:
        d = Toplevel(bg="black")
        label = Label(d, text="BOO!", bg="black", fg="white", font=('fixedsys', 17)).pack()
        def close():
            d.destroy()
        Button(d, bg="black", fg="white", width=10, activeforeground="grey", activebackground="black", text="Close", command=close).pack()

    elif 'how are you' in query:
        speak("Im doing well, thanks for asking")

    elif 'exit' in query or 'quit' in query:
        speak("Goodbye sir, have a good day")
        window.quit()
    
    elif query == '':
        speak("Please write something down")

    else:
        speak("Sorry sir, I cannot understand")

# Additional functions for the button commands
def you():
    speak("I will open it for you")
    webbrowser.open("https://www.linkedin.com/in/khalidalenizy/")

def win():
    speak("Ok sir, I will open it")
    webbrowser.open("https://github.com/khalzin0")

# Main function to set up the UI
def main():
    global ques
    # Canvas setup
    canvas = Canvas(window, width = 400, height = 230, bg='#0366fc') 
    canvas.pack(fill= "both", expand=True)
    label = Label(text="J.A.R.V.I.S made by Khalid Alenizy", bg="black", fg="white", font=('fixedsys', 17)).pack()
    # Entry for user input
    ques = Entry(window, width=30, bg="black", fg="lightblue", font=('fixedsys', 17, 'bold'))
    ques.pack(padx=10, pady=20)
    # Buttons for various commands
    Button(text="Execute Command", bg="#0366fc", fg="white", width=25, activeforeground="grey", activebackground="black", command=command, font=('fixedsys', 8)).pack(padx=0, pady=10)
    Button(text="Open Khalid's LinkedIn", bg="#0366fc", fg="white", width=25, activeforeground="grey", activebackground="black", command=you, font=('fixedsys', 8)).pack(pady=10)
    Button(text="Open Khalid's GitHub", bg="#0366fc", fg="white", width=25, activeforeground="grey", activebackground="black", command=win, font=('fixedsys', 8)).pack(side=BOTTOM, pady=10)

    
if __name__ == "__main__":
    main()

window.mainloop()