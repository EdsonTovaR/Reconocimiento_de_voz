import pyaudio
import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup
import datetime
import os
import webbrowser
import tkinter as tk

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Define function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to get current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

# Define function to get current weather
def get_weather():
    url = "https://www.weather.com/weather/today/l/USNY0996:1:US"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    temp = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ').text
    desc = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr').text
    return f"The current temperature is {temp} and the weather is {desc}."

# Define function to open a web page
def open_webpage(url):
    webbrowser.open(url)

# Define tkinter interface
root = tk.Tk()
root.title("Chatbot")

# Create text box to display chat history
chat_history = tk.Text(root, width=50, height=20)
chat_history.pack()

# Create entry box for user input
user_input = tk.Entry(root, width=50)
user_input.pack()

# Define function to handle user input and generate responses
def handle_input():
    # Get user input
    user_text = user_input.get()
    # Add user input to chat history
    chat_history.insert(tk.END, f"You: {user_text}\n")
    # Clear user input box
    user_input.delete(0, tk.END)
    # Generate response from chatbot
    if "tiempo" in user_text:
        response = f"The current time is {get_time()}."
    elif "clima" in user_text:
        response = get_weather()
    elif "musica" in user_text:
        response = "Opening Spotify..."
        open_webpage("https://www.spotify.com/")
    else:
        response = "I'm sorry, I didn't understand that."
    # Add chatbot response to chat history
    chat_history.insert(tk.END, f"Chatbot: {response}\n")
    # Speak chatbot response
    speak(response)

# Add button to submit user input
submit_button = tk.Button(root, text="Submit", command=handle_input)
submit_button.pack()

# Add functionality to listen for voice commands
def listen_for_commands():
    while True:
        command = recognize_speech().lower()
        if "hey chatbot" in command:
            speak("How can I help you?")
            user_input.focus()
            break

# Start listening for voice commands
listen_for_commands()

# Start tkinter main loop
root.mainloop()
