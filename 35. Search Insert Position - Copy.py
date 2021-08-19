


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        
        nums.sort()

        print(nums)
        return nums.index(target)

        """
        把a = a.append(b)改为a.append(b)后问题解决。
        原因：append会修改a本身，并且返回None。不能把返回值再赋值给a。
        """

c = Solution()
nums = [1,3,5,6]
target = 2
print(c.searchInsert(nums, target))
