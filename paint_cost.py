'''New question (Less Difficult)

Now say you can no longer buy fractions of a gallon. (For instance, if you need 4.3 gallons to do a project, then you have to buy 5 gallons of paint.)

With this new scenario, you will create a new function get_actual_cost that uses the same inputs and calculates the cost of your project.

One function that you'll need to use to do this is math.ceil(). We demonstrate usage of this function in the code cell below. It takes as a number as input and rounds the number up to the nearest integer.

Run the next code cell to test this function for yourself. Feel free to change the value of test_value and make sure math.ceil() returns the number you expect.'''
import math

test_value = 1.1

rounded_value = math.ceil(test_value)
print(rounded_value)

'''Use the next code cell to define the function get_actual_cost(). You'll need to use the math.ceil() function to do this.

When answering this question, note that it's completely valid to define a function that makes use of another function. For instance, we can define a function round_up_and_divide_by_three that makes use of the math.ceil function:'''

def round_up_and_divide_by_three(num):
    new_value = math.ceil(num)
    final_value = new_value / 3
    return final_value

# Solution ---->

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    gallons_to_buy = math.ceil(gallons_needed)
    cost = cost_per_gallon * gallons_to_buy
    return cost
