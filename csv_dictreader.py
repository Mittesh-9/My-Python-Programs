import csv

with open("", "r") as file:
    reader = csv.DictReader(file)
    counts = {} # or dict()

    for row in reader:
        favorite = row["language"]

        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1


for favorite in sorted(counts, key=counts.get, reverse=True): # key=counts.get this will allow it to apply it to the values of the dict
    print(f"{favorite}: {counts[favorite]}")