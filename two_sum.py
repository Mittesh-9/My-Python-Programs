
nums = [2,7,11,15]
target = 9

# nums = [3,2,4]
# target = 6

# Brute force solution > O(n^2)

n = len(nums)
for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print([i,j])
        # print([])


# Hashmap solution > O(n)

hashMap = {}

for i in range(len(nums)):
    hashMap[nums[i]] = i

print(hashMap)

