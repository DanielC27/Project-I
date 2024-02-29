import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo 
import statistics
from numpy import var

airquality_uci = "AirQualityUCI.csv"
dataframe = pd.read_csv(airquality_uci)
mediana = np.median(dataframe)
varianza = np.var(dataframe)

print("La mediana es: ", mediana)
print("La varianza es: ", varianza)