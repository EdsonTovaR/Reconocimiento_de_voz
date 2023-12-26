import librosa
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#Funcion para extraer caracteristicas de audio utilizando librosa
def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(mfccs.T, axis=0)
#Directorio que contiene grabaciones de voz por persona
data_dir = "Mi_directorio_de_datos"
#Lista para almacenar las caracteristicas y las etiquetas
features = []
labels = []
#Recorre las grabaciones y extrae caracteristicas 
for person in ["persona1", "persona2"]:
    for i in range(1,2): #Suponiendo que tiene 5 por persona 
        file_path = f"{data_dir}/{person}/{i}.wav"
        feature = extract_features(file_path)
        features.append(feature)
        labels.append(person)
#Convierte las listas a matrices numpy
X = np.array(features)
y = np.array(labels)
#Divide el conjunto de datos en conjuntos de entrenamiento y prueba 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Normaliza los datos (opcional, pero puede mejorar el rendimiento)
#Puedes utilizar StandardScaler de scikit-learn
#Crea y entrena el modelo k-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
#Realiza predicciones en el conjunto de prueba
y_pred = knn.predict(X_test)
#Evalua el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}') 