# 1) Identify the bug in the below code. 

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False

Solution -->

# Remember that return causes a function to exit immediately. So our original implementation always ran for just one iteration. We can only return False if we've looked at every element of the list (and confirmed that none of them are lucky). Though we can return early if the answer is True 

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

# 2) def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """

Solution -->

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    bool_list = []
    for i in L:
        if i > thresh  :
            bool_list.append(True)
        else:
            bool_list.append(False)
    return(bool_list)

# Better solutions by kaggle

def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res
    
# And here's the list comprehension version:

def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]

#  3) def menu_is_boring(meals):
   ''' Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.'''

Solution -->

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    prev_meal = None
    for meal in meals:
        if meal == prev_meal:
            return True
        prev_meal = meal
    return False

# Better solutions by kaggle

def menu_is_boring(meals):
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
# The key to our solution is the call to range. range(len(meals)) would give us all the indices of meals. If we had used that range, the last iteration of the loop would be comparing the last element to the element after it, which is... IndexError! range(len(meals)-1) gives us all the indices except the index of the last element.

# But don't we need to check if meals is empty? Turns out that range(0) == range(-1) - they're both empty. So if meals has length 0 or 1, we just won't do any iterations of our for loop.
