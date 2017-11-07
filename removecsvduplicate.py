import csv

with open('Download.csv',newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row[1])  # retrive the email value