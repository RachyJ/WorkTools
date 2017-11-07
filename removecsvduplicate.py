import csv
import pandas as pd

in_file = 'files/Download.csv'
output_file = 'files/2.csv'

df = pd.read_csv(in_file)
df.drop_duplicates(subset=['Email','Product'], inplace=True)
df.to_csv(output_file)
        