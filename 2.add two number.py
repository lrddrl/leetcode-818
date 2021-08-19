# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0        
        dummy = ListNode()
        #创立起始点
        curr = dummy
        while l1 != None or l2 != None:
            if l1 != None:
            #如果l1上面还有值，carry加上l1的值
                carry += l1.val
            #移动l1的指针道l1.next
                l1 = l1.next
            if l2 != None:  
            #如果l1上面还有值，那carry再加上l1的值
                carry += l2.val
                l2 = l2.next
            #旧节点curr指针指向，新的节点curr，值是carry % 10
            curr.next = ListNode(carry % 10)
            carry = 1 if carry >= 10 else 0
            #因为curr.next指向的新节点，
            #所以将新的节点重新赋值给 curr点
            curr = curr.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy.next


#l1
NodeA = ListNode(2)
NodeB = ListNode(4)
NodeA.next = NodeB

NodeC = ListNode(3)
NodeB.next = NodeC

#l2
NodeD = ListNode(5)
NodeE = ListNode(6)
NodeD.next = NodeE

NodeF = ListNode(4)
NodeE.next = NodeF

l1 = NodeA
l2 = NodeD

c = Solution()
print(c.addTwoNumbers(l1,l2).val)