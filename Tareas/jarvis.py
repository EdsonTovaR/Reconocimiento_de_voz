import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json




assistant_name = 'flix'
key = 'AIzaSyD4_jylymdL1tJTqOJl_gCMQi-EbsARt2A'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            talk("¿Que quieres que reproduzca?")
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-MX')
            rec = rec.lower()
            if assistant_name in rec:
                rec = rec.replace(assistant_name,'')
                print(rec)
            
    except:
        pass
    return rec

def run():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("No entendi, intenta de nuevo")
            continue
        if 'reproduce' in rec:
            
            music = rec.replace('reproduce','')
            talk('Reproduciendo '+ music)
            pywhatkit.playonyt(music)
            
        if 'cuantos suscriptores tiene' in rec:
            name_subs = rec.replace('cuantos suscriptores tiene','').strip()
            data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername'+ name_subs + '&key=' + key).read()
            subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            talk(name_subs + "tiene {:,d}".format(int(subs)) + "suscriptores")

        return pywhatkit.playonyt(music)


