import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import kagglehub

# %matplotlib inline

# download latest version
path = kagglehub.dataset_download("harlfoxem/housesalesprediction")
print("Path to dataset files:", path)

# dataset = pd.read_csv('../data/kc_house_data.csv')
#dataset.head() 

# dropping irrelevant columns
#dataset = dataset.drop(['id', 'date'], axis = 1)

