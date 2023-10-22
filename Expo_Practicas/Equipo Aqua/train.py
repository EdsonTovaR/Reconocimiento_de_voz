import os

import numpy as np 
from cargar import extract_features_from_file

def train():
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
    from model import get_model, save_model

    voice_model = get_model()

    voice_model.fit(X,Y,epochs=100,batch_size=1)
    save_model(voice_model)

if __name__ == "__main__":
    train()