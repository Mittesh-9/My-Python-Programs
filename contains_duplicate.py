nums = [1,3,2,1]
sorted = nums.sort()
print(sorted)

def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
        return False

containsDuplicate(nums)