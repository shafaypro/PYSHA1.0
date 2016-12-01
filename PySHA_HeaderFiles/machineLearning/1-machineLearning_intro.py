import pandas as pd
import sklearn
import numpy
import quandl

data_frame = quandl.get("WIKI/GOOGL") # getting the data frame from the quandl api to get the data
print(data_frame.head())