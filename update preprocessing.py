#!/usr/bin/env python3

# Timothy Nguyen
# preprocessing.py - modify movie dataset so it's suitable for classification

import pandas as pd
import numpy as np
from dateutil import parser     # used for different date formats


df = pd.read_csv(r'F:\dataset fyp 5 july 2021\intern copy of check new se.csv',encoding='ISO-8859-1')


df = df.drop_duplicates()




# create success column
# movie is successful if (revenue >= budget * 2)
for index, row in df.iterrows():
    try:
        budget = df.at[index, 'budget']
        revenue = df.at[index, 'revenue']
        if (revenue >= budget * 2):
            success = True
        else:
            success = False
    except:     # if budget or revenue is empty
        success = np.nan

    df.at[index, 'success'] = success





df.to_csv(r'F:\dataset fyp 5 july 2021\update 5 july 2021 copy of check new se.csv',encoding='ISO-8859-1', index=False)
print('Preprocessing Finished')
