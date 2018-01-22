import csv
import pandas as pd
from sys import argv
from pandas.io.excel import ExcelWriter

script, infile = argv  # take arguments from command line

output_file = infile.split('.')[0] + '.xlsx'  # use the same file name as output

df = pd.read_csv(infile, encoding='ISO-8859-1') # consider index_col=False to force pandas to not use the first column as the index (row names)
df.drop_duplicates(subset=['Email','Product'], inplace=True)  # remove duplicates by email + product; drop duplicates

columns2delete = set(['Choose','Delete']) # invalid columns
if columns2delete.issubset(df.columns):
    for e in columns2delete:
        del df[e]

# if df.columns.str.contains('dynamsoft.com'):

order_columns = set(['Pay Date'])
if order_columns.issubset(df.columns):

    start_column = df.columns.get_loc('Ticket No.')
    end_column = len(df.columns)
    col = list(df.columns)[start_column-1:end_column]
    df.drop(col, axis=1, inplace=True)


with ExcelWriter(output_file) as ew:
    df.to_excel(ew, index=False)  # index=False no extra index column
        