import os
import pathlib
import src

NUM_INPUTS = 2
NUM_LAYERS = 3
P = [NUM_INPUTS,2,1]

f = [None, "relu","sigmoid"]

LOSS_FUNCTION = "Binary Cross Entropy Loss"
MINI_BATCH_SIZE = 2

PACKAGE_ROOT = pathlib.PATH(src.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT , "datasets")