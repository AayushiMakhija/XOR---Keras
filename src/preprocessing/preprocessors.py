import numpy as np
import os

from src.config import config
from src.preprocessing.data_management import load_dataset

training_data = load_dataset("train.csv")

mb_size = 2

X_train = training_data.iloc[:,0:2]
Y_train = training_data.iloc[:,2]

X_train = np.array(X_train)
Y_train = np.array(Y_train)
Y_train = Y_train.reshape(Y_train.shape[0],1)

def training_data_generator():

    for i in range(training_data.shape[0]//mb_size):

        X_train_mb = X_train[i*mb_size:(i+1)*mb_size,:]
        Y_train_mb = Y_train[i*mb_size:(i+1)*mb_size,:]

        yield X_train_mb, Y_train_mb