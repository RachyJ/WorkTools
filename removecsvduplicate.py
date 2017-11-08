import csv
import pandas as pd
from sys import argv
from pandas.io.excel import ExcelWriter

script, infile = argv  # take arguments from command line

#in_file = 'files/Download.csv'
#output_file = 'files/2.csv'

in_file = infile
index = in_file.find('.')
output_file = in_file[0:index] + '.xlsx' # use the same file name for export

df = pd.read_csv(in_file)
df.drop_duplicates(subset=['Email','Product'], inplace=True)  # remove duplicates by email + product

with ExcelWriter(output_file) as ew:
    df.to_excel(ew, index=False)  # index=False no extra index column
        