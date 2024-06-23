import os 
import pandas as pd

from src.config import config

def load_dataset(file_name):
    
    file_path = os.path.join(config.DATAPATH, file_name)
    
    data = pd.read_csv(file_path)
    
    return data

