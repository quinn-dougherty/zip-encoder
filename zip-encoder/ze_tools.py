"""zip-encoder tools"""

import altair as alt
import pandas as pd
from toydat import DF

class map: 
    def __init__(self, dat, remove_outliers=False, sample_size=None):
        if sample_size is not None:
            self.dat = dat.sample(sample_size)
        else: 
            self.dat = dat



def show_map(dat=DF, remove_outliers=False, sample_size=None):
    '''show the basic map'''

    if sample_size is not None:
        C_ = alt.Chart(dat.sample(sample_size)).mark_circle().encode(color='TARGET', tooltip='TARGET')
    else:
        C_ = alt.Chart(dat).mark_circle().encode(color='TARGET')

    def rmv_outliers():
        return C_.encode(x='latitude',y='longitude')

    def keep_outliers():
        return C_.encode(x='latitude',y='longitude')

    if remove_outliers:
        return rmv_outliers()
    if not remove_outliers:
        return keep_outliers()
