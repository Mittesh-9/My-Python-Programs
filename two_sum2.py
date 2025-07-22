# Two Sum II - Input Array Is Sorted

def twoSum(nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = 1

        # THIS WORKS FINE UNTIL DUPLICATES FOUND IN THE ARRAY
        while r < len(nums):
                if nums[l] + nums[r] == target:
                        l_num = nums.index(nums[l], l, r) + 1
                        r_num = nums.index(nums[r], l, r + 1) + 1
                        target_list = [l_num, r_num]
                        print(target_list)
                else:
                        r += 1
                        continue
                break
        
        # THIS IS CORRECT
        l, r = 0, len(numbers) - 1
        while l < r:
                s = numbers[l] + numbers[r]
                if s == target:
                        return [l + 1, r + 1]
                elif s < target:
                        l += 1
                else:
                        r -= 1
        # Added fallback (technically unreachable if input is valid)
        return [-1, -1]
        
        
nums = [-1,0]
target = -1

twoSum(nums, target)


'''

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

numbers = [0,0,3,4]

target = 0
'''