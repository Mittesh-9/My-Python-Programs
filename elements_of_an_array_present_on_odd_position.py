# initialize an array
array = [1,2,3,4,5,6,7,8,9,10]

# ALGORITHM:
# STEP 1: Declare and initialize an array.
# STEP 2: Calculate the length of the declared array.
# STEP 3: Loop through the array by initializing the value of variable "i" to 0 then incrementing its value by 2, i.e., i=i+2.
# STEP 4: Print the elements present in odd positions.

print("Elements of given array present on odd position: ")

for i in range(0, len(array), 2)
    print(array[i])
