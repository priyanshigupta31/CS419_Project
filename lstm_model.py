from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout


def build_improved_model(input_dim, output_dim, return_sequences):
    # Builds an improved LSTM using keras.layers.recurrent.lstm
    model = Sequential()
    model.add(LSTM(
        input_shape=(None, input_dim),
        units=output_dim,
        return_sequences=return_sequences))

    model.add(Dropout(0.2))

    model.add(LSTM(
        128,
        return_sequences=False))

    model.add(Dropout(0.2))

    model.add(Dense(
        units=1))
    model.add(Activation('linear'))

    return model   


def basic_model(ip_dim, op_dim, return_sequences):
    # Builds a basic lstm model 
    model = Sequential()
    model.add(LSTM(
        input_shape=(None, ip_dim),
        units= op_dim,
        return_sequences=return_sequences))

    model.add(LSTM(
        100,
        return_sequences=False))

    model.add(Dense(
        units=1))
    model.add(Activation('linear'))

    return model  


