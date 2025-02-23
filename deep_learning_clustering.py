# deep_learning_clustering.py

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Define autoencoder for DEC
input_layer = Input(shape=(input_dim,))
encoded = Dense(64, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='sigmoid')(encoded)

autoencoder = Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='mse')