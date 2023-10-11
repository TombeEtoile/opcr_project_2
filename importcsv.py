import csv

with open("fichier.csv", mode="r+") as file:
    importcsv = csv.DictReader(file)
    for line in importcsv:
        print(line)