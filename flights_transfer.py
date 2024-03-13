import csv
# flights.csv was too large for git, this script is for splitting it into smaller pieces
print("Reading original file ...")
with open("flights.csv", "rt", encoding='iso-8859-1') as f:
    flights = list(csv.reader(f, delimiter=","))
print("Read complete!")

print("Creating new contents ...")
new_csv = ""
for row in flights:
    newRow = row[1] + "," + row[7] + "," + row[8] + "," + row[11] + "\n"
    new_csv += newRow

print("Finished copying contents!")
print("Writing to new CSV file ...")
with open(f"flight_delays1.csv", 'w', encoding='utf-8') as new_file:
    new_file.write(new_csv)
print("Completed!")

