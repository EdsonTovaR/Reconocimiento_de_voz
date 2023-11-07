import speech_recognition as sr

def reconocer_voz_y_guardar():
    # Crear un objeto de reconocimiento de voz
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as source:
        print("Hable para comenzar a reconocer la voz...")
        audio = r.listen(source)
        print("Escuchado, ahora reconociendo...")

    try:
        # Reconocer la voz usando el reconocedor de voz de Google
        texto_reconocido = r.recognize_google(audio, language="es-ES")
        print("Texto reconocido: " + texto_reconocido)

        # Guardar la transcripción en un archivo de texto
        with open("transcripcion.txt", "a") as archivo:
            archivo.write(texto_reconocido + "\n")
        print("Transcripción guardada en 'transcripcion.txt'")

    except sr.UnknownValueError:
        print("No se pudo entender lo que dijiste")
    except sr.RequestError as e:
        print("Error al conectarse al servicio de reconocimiento de voz: {0}".format(e))


if __name__ == "__main__":
    reconocer_voz_y_guardar()
