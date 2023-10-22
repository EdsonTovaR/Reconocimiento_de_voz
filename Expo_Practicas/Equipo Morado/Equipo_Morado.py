import speech_recognition as sr
import numpy as np
from hmmlearn import hmm

# Datos de entrenamiento ficticios para un modelo HMM de tres estados
training_data = np.array([0, 0, 1, 1, 2, 2]).reshape(-1, 1)

# Crear y entrenar el modelo HMM
model = hmm.GaussianHMM(n_components=3, covariance_type="full", n_iter=100)
model.fit(training_data)

# Secuencia de observaciones de entrada (puedes reemplazar esto con una grabación de voz)
input_sequence = np.array([0, 1, 2]).reshape(-1, 1)

# Realizar la predicción de la secuencia de entrada
predicted_states = model.predict(input_sequence)
print("Secuencia de estados predicha:", predicted_states)


# Inicializa el reconocedor de voz
recognizer = sr.Recognizer()

# Captura audio del micrófono
with sr.Microphone() as source:
    print("Habla algo...")
    audio = recognizer.listen(source)

# Utiliza el motor de reconocimiento de Google para convertir el audio en texto
try:
    text = recognizer.recognize_google(audio)
    print("Texto reconocido: " + text)
except sr.UnknownValueError:
    print("No se pudo reconocer el audio")
except sr.RequestError as e:
    print("Error en la solicitud al servicio de reconocimiento de voz: {0}".format(e))
