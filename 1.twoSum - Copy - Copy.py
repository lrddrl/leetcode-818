"""
Spyder Editor

This is a temporary script file.
"""


"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

"""

class Solution:
    def twoSum(self,nums,target):
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index:]
            if j in temp_nums:
                return [start_index, temp_nums.index(j)+ next_index]
                

    


nums = [2, 7, 11, 15]
solution1 = Solution()
print(solution1.twoSum(nums,22))
