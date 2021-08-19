# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

"""

#题目解析，找到符合目标值的索引。

class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            # 目标的两个数分别为 i 和 j，所以i+j = 9
            #从第一个i开始每个数开始找，第一个i = 2，所以要找到的j应该是7       
            j = target - i #7 = 9 - 2        
            start_index = nums.index(i) 
            #首先，先找i的索引，开始索引是0： start_index = nums.index(i) = 0，            
            next_index = start_index + 1 
            #有了i的索引以后，结下来要找目标j的索引，
            #j的索引肯定不是0，所以是从0开始的下一位，所以是0+1
            temp_nums = nums[next_index: ] 
            # 1 应该先找到j的值，以它的索引建立一个列表。【7，11，15】
            # （额外：假如目标值是17，那么j的值就是15，它在临时列表里的索引就是2
            if j in temp_nums:
                return(nums.index(i), next_index + temp_nums.index(j))
            #next_index + temp_nums.index(j) 解释
            # 比如j的值是7，next_index的索引是 1=0+1， temp_nums.index(2)的索引是0，所以最终j的索引是 1=0+1+0
            #所以最终索引答案是【index(i),index(j)】 = [0,1]
     
c = Solution()
print(c.twoSum([2,7,11,15],9))





#完整的代码


class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index: ]
            if j in temp_nums:
                return(nums.index(i), next_index + temp_nums.index(j))
            
     
c = Solution()
print(c.twoSum([2,7,11,15],9))





这是leetcode python的第一题，code来自于，未取得授权，仅仅是个人日记用。
https://www.youtube.com/watch?v=OTtbG8lNNW8
Michelle小梦想家






"""
from typing import List
       
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
      c = {}
      for idx,num in enumerate(nums):
          cur = target - num
          if num in c:
              return [c[num],idx]
          c[cur] = idx
              
c = Solution()
print(c.twoSum([2,7,11,15],9))

"""
