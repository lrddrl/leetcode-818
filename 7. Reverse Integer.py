# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:43:35 2020

@author: ruodo
"""


"""
leetcode 第7题，颠倒整数
"""

class Solution:
    def reverse(self,x):
        # 范围-214783648~214783647
        num = 0
        
        #返回绝对整数
        a = abs(x)
        
        
            # 假设 有个123
            # a = 123
            # nume = 0
            # 第一次迭代的时候
            # a = 12
            # num =3
            # 第二次迭代的时候
            # a = 1
            # num = 32
            #第三次迭代的时候
            # a = 0
            #num = 321
        while(a != 0):
            #需要一个中间值，对a取模
            #取模就是得到a的余数，比如 321除10，得32 余数是1
            #就得到我们想要的1了
            temp = a % 10
            num = num * 10 + temp
            a = int(a/10)
            
        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= -2147483647:
            return -num
        else:return 0

c = Solution()
print(c.reverse(1864))





