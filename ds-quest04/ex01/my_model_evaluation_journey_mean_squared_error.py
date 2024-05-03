import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

def my_model_evaluation_journey_mean_squared_error(param_1, param_2):
    df1 = pd.read_csv(param_1,  header=0)
    df2 = pd.read_csv(param_2,  header=0)
    
    if df1.shape != df2.shape:
        df2 = df2[df2.index < df1.shape[0]]
    
    df1.drop('robot_model_name', axis=1, inplace=True)
    df2.drop('robot_model_name', axis=1, inplace=True)
    
    javob = mean_squared_error(df1, df2)
    return javob
