'''Question --- 

	You work for a company that provides data services. For $100/month, your company provides 15 gigabytes (GB) of data. Then, any additional data is billed at $0.10/MB (or $100/GB, since 1,000 MB are in 1 GB).

Use the next code cell to write a function get_phone_bill() that takes as input:

gb = number of GB that the customer used in a month
It should return the customer's total phone bill.

For instance:

A customer who uses 10 GB of data in one month is billed only $100, since the usage stayed under 15 GB. In other words, get_phone_bill(10) should return 100.
A customer who uses 15.1 GB (or 15 GB + 100 MB) of data in one month has gone over by .1 GB, so they must pay $100 (cost of plan), plus $0.10 * 100 = $10, for a total bill of $110. In other words, get_phone_bill(15.1) should return 110.
Do not round your answer.'''

# Solution --->

def get_phone_bill(gb):
    if gb <= 15:
        bill =  100
    else:
        bill = 100 + (gb - 15) * 100
    return bill