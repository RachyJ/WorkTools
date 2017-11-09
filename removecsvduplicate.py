import csv
import pandas as pd
from sys import argv
from pandas.io.excel import ExcelWriter

script, infile = argv  # take arguments from command line

output_file = infile.split('.')[0] + '.xlsx'  # use the same file name as output

df = pd.read_csv(infile)
df.drop_duplicates(subset=['Email','Product'], inplace=True)  # remove duplicates by email + product

with ExcelWriter(output_file) as ew:
    df.to_excel(ew, index=False)  # index=False no extra index column
        