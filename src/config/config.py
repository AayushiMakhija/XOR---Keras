import os
import pathlib
import src

from keras.optimizers import RMSprop

optimizer = RMSprop

epochs = 1000

mb_size = 2


PACKAGE_ROOT = pathlib.PATH(src.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT , "datasets")

SAVED_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_models")