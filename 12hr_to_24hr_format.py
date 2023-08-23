# Python program to convert time from 12 hour to 24 hour format

def convert24(str1):
    # Checking if last two elements of time is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    
    # Removing the AM
    elif str1[-2] == "AM":
        return str[:-2]
    
    # Checking if last two elements of time is PM or first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        # Add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]
    
# Driver Code
print(convert24("09:09:50 PM"))