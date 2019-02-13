"""module docstring

I wanted to do this in a one-liner but 
ValueError: Length of values does not match length of index<Paste>

module docstring"""

import pandas as pd

COLUMNS = ['id', 'latitude', 'longitude']

ys= pd.read_csv('toydat/train_labels.csv').drop('id', axis=1).to_numpy()

DF = (pd.read_csv('toydat/train_features.csv').loc[:, COLUMNS])#

DF.insert(0, 'TARGET', ys)

assert all([x==0 for x in DF.isna().sum()])



