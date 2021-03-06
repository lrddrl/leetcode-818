# -*- coding: utf-8 -*-


"""
Given an array nums of n integers, are there elements a, b, c
 in nums such that a + b + c = 0? 
 
 Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""

#题目解析，找到符合目标值的索引。

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)   
        result = []
        nums.sort()

        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+1] > 0:
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            if 0 < i and nums[i] == nums[i-1]:
                continue
            l,r  = i+1 , n-1
            while l < r :
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0 :
                    result.append([nums[i], nums[l], nums[r]])
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while l < r-1 and nums[r] == nums[r-1]:
                        r -=1
                    r -= 1
                elif tmp <0:
                    l += 1
                else:
                    r -= 1
        return result


c = Solution()
print(c.threeSum([-1,0,1,2,-1,-4]))

# [-1,0,1,2,-1,-4]