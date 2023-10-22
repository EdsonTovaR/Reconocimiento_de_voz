from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten, Conv1D, MaxPooling1D, Reshape, Input
import os

model_path = os.path.join('models','model2.h5')
weights_path = os.path.join('models','model_weights2.h5')

def get_model():
    if os.path.exists(model_path):
        model = load_model(model_path)
        model.load_weights(weights_path)
    else:
        """ model = Sequential()
        model.add(Dense(193, input_shape=(193,), activation = 'relu'))
        model.add(Dropout(0.1))
        model.add(Dense(128, activation = 'relu'))
        model.add(Dropout(0.25))  
        model.add(Dense(128, activation = 'relu'))
        model.add(Dropout(0.5))    
        model.add(Dense(1, activation = 'sigmoid'))##<-- numero de categorias a predecir """
        model = Sequential([
        Input(shape=(40,)),
        Reshape((40, 1)),
        Conv1D(32, kernel_size=2, activation='relu'),
        MaxPooling1D(pool_size=2),
        Dropout(0.25),
        Conv1D(64, kernel_size=2, activation='relu'),
        MaxPooling1D(pool_size=2),
        Dropout(0.5),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')  # 2 clases: hombre y mujer
    ])
    model.compile(loss='binary_crossentropy', metrics=['Precision', 'accuracy'], optimizer='adam')

    return model

def save_model(model):
    model.save(model_path)
    model.save_weights(weights_path)


import numpy as np 
from cargar import extract_features_from_file

def train(model):
    path = os.path.join('audios','defaults')
    X = []
    Y = []
    for file in os.listdir(path):
        features, _ = extract_features_from_file(os.path.join(path,file))
        print(features.shape)
        X.append(features)
        Y.append(np.zeros(1,))
    print(Y)
    from cargar import get_autdios_features
    x_user, y_user = get_autdios_features()
    X.extend(x_user)
    Y.extend(y_user)

    X = np.array(X)
    Y = np.array(Y)

    model.fit(X,Y,epochs=600,batch_size=1)
    save_model(model)