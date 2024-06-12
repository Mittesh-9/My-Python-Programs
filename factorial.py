user_input = int(input('Enter the number : '))

def factorial(user_input):

    numbers_list = []

    if user_input == 0 or user_input == 1:
        print (1)
    
    else:
        for i in range(2 ,user_input + 1): # user_input + 1 >> To include user_input
            numbers_list.append(i)
            actual_factorial = 1
            for j in numbers_list:
                # actual_factorial = actual_factorial * j 

                # OR

                actual_factorial *= j
                
                # OR

                # return user_input * factorial(user_input - 1) >>  Recursive approach

    # You don't need to store the numbers in a list and then iterate over the list. You can directly multiply the numbers in the range.
    # else:
    #     actual_factorial = 1
    #     for i in range(2, user_input + 1):
    #         actual_factorial *= i
    #     return actual_factorial

    print(actual_factorial)


try:
    user_number = int(user_input)
    # Call the function with the user's number
    factorial(user_number)
except ValueError:
    print("Please enter a valid integer.")

# OR

# if __name__ == '__main__':
#     user_input = int(input('Enter the number : '))
#     fac = factorial(user_input)
#     print(f'The factorial of the number {user_input} is {fac}')
