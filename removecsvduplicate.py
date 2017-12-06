import csv
import pandas as pd
from sys import argv
from pandas.io.excel import ExcelWriter

script, infile = argv  # take arguments from command line

output_file = infile.split('.')[0] + '.xlsx'  # use the same file name as output

df = pd.read_csv(infile, encoding='ISO-8859-1')
df.drop_duplicates(subset=['Email','Product'], inplace=True)  # remove duplicates by email + product

# columns2delete = set(['Choose','Delete','Pay Date','Order Type','Reseller Country','Total Without Tax','Tax Fee','Upgrade Fee','YS Fee','Late Payment Fee','Technical Contact Email','Technical Contact Name','Labels1'])

# special_columns = set(['Ticket No.','Add-on Fee','Discount (%)','Discount($)'])
# columns2delete2 = special_columns.filter(regex='Ticket No|Discount|Add on Fee ').columns

columns2delete = set(['Choose','Delete']) # invalid columns
if columns2delete.issubset(df.columns):
    for e in columns2delete:
        del df[e]

order_columns = set(['Pay Date'])
if order_columns.issubset(df.columns):
    print('this is the order report')

with ExcelWriter(output_file) as ew:
    df.to_excel(ew, index=False)  # index=False no extra index column
        