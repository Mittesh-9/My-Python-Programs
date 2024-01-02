import statistics as sc

# mean function >> The mean() function is used to calculate the arithmetic mean of the numbers in the list

# list of positive integer numbers   
dataset = [5, 2, 7, 4, 2, 6, 8]     
x = sc.mean(dataset)     
# Printing the mean   
print("Mean is :", x)

# median function >> The median() function is used to return the middle value of the numeric data in the list

dataset = [4, -5, 6, 6, 9, 4, 5, -2]      
# Printing median of the random data-set   
print("Median of data-set is : % s "  
        % (sc.median(dataset)))  

# mode function >> The mode() function returns the most common data that occurs in the list

# declaring a simple data-set consisting of real valued positive integers.   
dataset =[2, 4, 7, 7, 2, 2, 3, 6, 6, 8]     
# Printing out the mode of given data-set   
print("Calculated Mode % s" % (sc.mode(dataset)))