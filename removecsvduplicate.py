import csv
import pandas as pd
from sys import argv

script, infile, outfile = argv

#in_file = 'files/Download.csv'
#output_file = 'files/2.csv'

in_file = infile
output_file = outfile

df = pd.read_csv(in_file)
df.drop_duplicates(subset=['Email','Product'], inplace=True)
df.to_csv(output_file)
        