# Kaggle code - After tax pay problem
'''def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax'''

def get_pay( num_hours ):
    pay_pretax = num_hours * 15
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

# Solution
pay_fulltime = get_pay(40)
print(pay_fulltime)

# pay_fulltime = get_pay(184) # 184 is the full month (8 * 23)
# print(pay_fulltime)

# print(pay_fulltime * 82)

# x = (1 - .12)
# print(x)