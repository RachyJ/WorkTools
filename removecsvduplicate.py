import csv
import pandas as pd
from sys import argv
from pandas.io.excel import ExcelWriter

script, infile, outfile = argv  # take arguments from command line

#in_file = 'files/Download.csv'
#output_file = 'files/2.csv'

in_file = infile
output_file = outfile

df = pd.read_csv(in_file)
df.drop_duplicates(subset=['Email','Product'], inplace=True)  # remove duplicates by email + product

with ExcelWriter(outfile) as ew:
    df.to_excel(ew)
        