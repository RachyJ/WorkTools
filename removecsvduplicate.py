import csv
import pandas as pd
from sys import argv
from pandas.io.excel import ExcelWriter

script, infile = argv  # take arguments from command line

output_file = infile.split('.')[0] + '.xlsx'  # use the same file name as output

df1 = pd.read_csv(infile, encoding='ISO-8859-1') 
df = pd.DataFrame(df1)
df = df[~df['Email'].str.contains('@dynamsoft.com', na=False)] # filter out the records from dynamsoft 
df.drop_duplicates(subset=['Email','Product'], inplace=True)  # remove duplicates by email + product

columns2delete = set(['Choose','Delete']) # invalid columns
if columns2delete.issubset(df.columns):
    for e in columns2delete:
        del df[e]

    # df.drop(columns2delete)

order_columns = set(['Pay Date'])
if order_columns.issubset(df.columns):

    start_column = df.columns.get_loc('Ticket No.')
    end_column = len(df.columns)
    col = list(df.columns)[start_column-1:end_column]
    df.drop(col, axis=1, inplace=True)


with ExcelWriter(output_file) as ew:
    df.to_excel(ew, index=False)  # index=False no extra index column
        