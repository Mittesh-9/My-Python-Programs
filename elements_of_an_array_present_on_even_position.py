# initialize an array
array = [1,2,3,4,5,6,7,8,9,10]

# ALGORITHM:
# STEP 1: Declare and initialize an array.
# STEP 2: Calculate the length of the declared array.
# STEP 3: Loop through the array by initializing the value of variable "i" to 1 (because first even positioned element lies on i = 1) then incrementing its value by 2, i.e., i=i+2.
# STEP 4: Print the elements present in even positions.

print("Elements of given array present on even position: ")

for i in range(1, len(arr), 2):    
    print(arr[i])
