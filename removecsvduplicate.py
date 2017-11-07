import csv

with open('Download.csv',newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row[1])  # retrive the email value in download export
        print(row[3])  # retrieve the product name in download export