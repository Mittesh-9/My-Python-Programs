import csv

MONTH = "give name" 

def fin_manager(file):

    transactions= []
    sum = 0

    with open(file, mode = "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None) # To skip the headers
        for row in csv_reader:
            name = row[2]
            amount = float(row[4])
            date = row[1]

            transaction = (date , name, amount)
            sum += amount
            transactions.append(transaction)

    print(f"The sum of all the transactions for the month {MONTH} is {sum}/n")
    return transactions

print(fin_manager(r"/home/mittesh/Downloads/Datasets/transaction.csv"))
    