import csv

with open("employees.csv", "a", encoding="utf-8") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Jenny Scoot", 2500])

