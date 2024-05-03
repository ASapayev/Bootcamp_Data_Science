import pandas as pd
import numpy as np
def my_pandas_journey_return_numeric_variables(param_1):
    ustun_nomi = param_1.columns

    is_numeric = param_1.dtypes.apply(lambda x: x in [np.int64, np.float64])

    numeric_columns = ustun_nomi[is_numeric]
    return param_1[numeric_columns]
