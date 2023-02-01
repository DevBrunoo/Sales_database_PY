import csv 

with open("heart.csv", "o2Saturation.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)