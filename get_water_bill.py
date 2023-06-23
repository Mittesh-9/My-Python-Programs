'''Question --- You are a programmer at a water agency. Recently, you have been tasked to write a function get_water_bill() that takes as input:

num_gallons = the number of gallons of water that a customer used that month. (This will always be an integer with no decimal part.)
It should output the water bill.

The water agency uses this pricing structure:

Tier	Amount in gallons	Price per 1000 gallons
Tier 1	0 - 8,000	$5
Tier 2	8,001 - 22,000	$6
Tier 3	22,001 - 30,000	$7
Tier 4	30,001+	$10
For example:

Someone who uses 10,000 gallons of water in a month is placed in Tier 2, and needs to pay a water bill of $6 * 10 = $60. In other words, get_water_bill(10000) should return 60.0.
Someone who uses 25,000 gallons of water in a month is placed in Tier 3, and needs to pay a water bill of $7 * 25 = $175. In other words, get_water_bill(25000) should return 175.0.
Do not round your answer. So, your answer might return fractions of a penny.'''

# Solution --->

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = (5 * num_gallons / 1000)
    elif num_gallons <= 22000:
        bill = (6 * num_gallons / 1000)
    elif num_gallons <= 30000:
        bill = (7 * num_gallons / 1000)
    else:
        bill = (10 * num_gallons / 1000)
    return bill