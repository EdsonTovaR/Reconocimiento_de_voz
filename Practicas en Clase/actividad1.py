import speech_recognition as sr

#Crea un objeto de reconocimiento de voz
recognizer=sr.Recognizer()

#Abre un archivo de texto
with open("Resultados.txt","w") as f:
    
    #Escuchamos al usuario
    audio = recognizer.listen()
    
    #Intentamos reconocer la voz
    try:
        #Obtiene el texto reconocido
        text=recognizer.recognize_google(audio)
        
        #Imprime el texto reconocido
        print(text)
        
        #Guarda el texto reconocido en el archivo
        f.write(str(text))
        
    except sr.UnknownValueError:
        print("No se pudo reconocer la voz")
    except sr.RequestError as e:
        print(f"Error de solicitud: {e}")