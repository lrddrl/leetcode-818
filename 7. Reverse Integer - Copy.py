class Solution:
    def reverse(self, x: str) -> str:
        #将整数的绝对值转换成字符串
        s=str((x))
        #翻转字符串
        s=s[::-1]
        #如果输入整数是负数，增加负号
        return s

c = Solution()
print(c.reverse("Ihave"))