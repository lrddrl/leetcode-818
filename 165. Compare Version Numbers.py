# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 07:47:03 2020

@author: ruodo
"""


class Solution:
    def compareVersion(self,version1:str,version2:str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        n = max(len(version1),len(version2))
        print("这是数字1",version1)
        print("这是数字2",version2)
        i = 0 #这个是索引
        # print("最大长度：",n)

        # a = range(n)
        # print("range(n)", a)
        
        
        for i in range(n):
            # b = len(version1)
            # print("len(version1)", b)
            # b = len(version2)
            # print("len(version2)", b)
            v1 = int(version1[i]) if i < len(version1) else None
            v2 = int(version2[i]) if i < len(version2) else None
            print("这是第几次循环：",i)
            print(v1)
            print(v2)
            if not v2 and v1:
                return 1
            elif not v1 and v2:
                return -1
            elif v1 and v2:
                if v1 > v2:
                    return 1
                elif v1 < v2:
                    return -1
        return 0
                
c = Solution()
print("""这是最终结果""",c.compareVersion("1.0","1.0.1"))  #这里要注意一下，用“”输入字符串，直接输入的是整数，会报错。



#  """这是leetcode python的第165题，code来自于，未取得授权，仅仅是个人日记用。
# https://www.youtube.com/watch?v=GNSTPuSBZFk
# Michelle小梦想家
# """



