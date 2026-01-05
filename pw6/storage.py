import os
import pickle
import gzip

def save_data(file_path, data):
    with gzip.open(file_path, 'wb') as f:
        pickle.dump(data, f)

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    
    with gzip.open(file_path, 'rb') as f:
        data = pickle.load(f)
    
    return data
