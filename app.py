import csv
import pandas as pd

df = pd.read_csv('input.csv')

new_df = df.iloc[:, [0, 2]] # For columns you need to extract

new_df.to_csv('output.csv', index=False)