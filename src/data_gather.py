'''
Function to gather csv files that have been saved in data folder below project
working directory.

INPUT: string value of the data directory name
OUTPUT: Pandas dataframe containing contents of all files from input directory
'''

import os
import pandas as pd


def data_gather(dir_string):
    all_files = [f for f in os.listdir(dir_string) if f.endswith('csv')]

    li = []

    for filename in all_files:
        df = pd.read_csv('data/' + filename, index_col=None, header=0)
        li.append(df)

    return pd.concat(li, axis=0, ignore_index=True)


