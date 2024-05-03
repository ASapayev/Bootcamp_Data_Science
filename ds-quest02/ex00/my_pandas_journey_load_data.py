from io import StringIO
from pandas import DataFrame as df
import pandas as pd
def my_pandas_journey_load_data(param_2):
    data = param_2
    df = pd.read_csv(data)
    return df