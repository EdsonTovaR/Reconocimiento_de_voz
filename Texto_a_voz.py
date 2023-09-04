import speech_recognition as sr
import pyttsx3

# Iniciamos el reconocedor de voz
r = sr.Recognizer()

#funcion para convertir el texto a voz
def SpeakText(command):
    # Iniciamos el motor de voz
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):
    try:
        # Usamos el microfono como fuente de audio
        with sr.Microphone() as source2:
            # Se ajusta el ruido de fondo
            r.adjust_for_ambient_noise(source2, duration=0.2)
            # Se lee el audio
            print("Escuchando...")
            audio2 = r.listen(source2)
            # Se reconoce el audio usando google
            MyText = r.recognize_google(audio2, language='es-ES')
            MyText = MyText.lower()

            print("Dijiste: "+MyText)
            SpeakText(MyText)
            break

    except sr.RequestError as e:
        print("No se pudieron solicitar resultados; {0}".format(e))
    except sr.UnknownValueError:
        print("Se produjo un error desconocido")


