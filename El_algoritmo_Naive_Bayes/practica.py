import os
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from python_speech_features import mfcc 
import librosa
# Función para extraer las características de audio utilizando MFCC
def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast') 
    mfccs = mfcc(audio, samplerate=sample_rate) 
    return np.mean(mfccs, axis=0)
#Directorio que contiene grabaciones de voz por persona
data_dir="tu_directorio_de_datos"
#Lista para almacenar las listas y las etiquetas
features=[]
labels=[]
#Recorre las grabaciones y extrae caracteristicas
for person in os.listdir(data_dir):
    person_dir = os.path.join(data_dir, person)
    if os.path.isdir(person_dir):
        for filename in os.listdir(person_dir):
            file_path = os.path.join(person_dir, filename)
            feature = extract_features(file_path)
            features.append(feature)
            labels.append(person)
#Convierte las lsitas a matrices numpy
X = np.array(features)
y = np.array(labels)
#Divide el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, n_samples=0, test_size=0.2, train_size=0, random_state=42)
#Crea y entrena el modelo de Naive Bayes
naive_bayes = GaussianNB()
naive_bayes.fit(X_train,y_train)
#Realiza predicciones en el conjunto de prueba 
y_pred= naive_bayes.predict(X_test)
accuracy =accuracy_score(y_test, y_pred) #Evalua el rendimiento del modelo
print(f'Accuracy: {accuracy}')

