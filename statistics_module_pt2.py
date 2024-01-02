import statistics as sc

# stdev function >> The stdev() function is used to calculate the standard deviation on a given sample which is available in the form of the list

# creating a simple data - set   
sample = [7, 8, 9, 10, 11]     
# Prints standard deviation   
print("Standard Deviation of sample is % s "   
                % (sc.stdev(sample)))

# median low function >> The median_low function is used to return the low median of numeric data in the list

# simple list of a set of integers   
set1 = [4, 6, 2, 5, 7, 7]     
# Note: low median will always be a member of the data-set.     
# Print low median of the data-set   
print("Low median of data-set is % s "   
        % (sc.median_low(set1)))

# median high function >> The median_high function is used to return the high median of numeric data in the list

# list of set of the integers   
dataset = [2, 1, 7, 6, 1, 9]     
print("High median of data-set is %s "   
        % (sc.median_high(dataset)))