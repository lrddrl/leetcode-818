# -*- coding: utf-8 -*-
"""
compare v1, v2
 if v1 > v2:
                    return 1
                elif v1 < v2:
                    return -1
"""

class Solution:
    def compareVersion(self, version1:str, version2:str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        n = max(len(version1),len(version2))

        for i in range(n):
            v1 = int(version1[i]) if i < len(version1) else None
            v2 = int(version2[i]) if i < len(version2) else None
            print("这是第几次循环：",i)
            print(v1)
            print(v2)
            if v1 and v2:
                if v1 > v2:
                    return 1
                elif v1 < v2:
                    return -1                
            elif not v1 and v2:
                return -1
            elif v1 and not v2:
                return 1            
        return 0

c = Solution()
print("""这是最终结果""",c.compareVersion("1.01","1.001"))
            