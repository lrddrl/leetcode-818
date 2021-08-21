class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


dummy = ListNode() 
curr = dummy

anothor = ListNode(6,dummy)  

# print(dummy.val)
# print(curr.val)
print(anothor.val)
print(anothor.next.val)

curr.val = 5

# print(dummy.val)
# print(curr.val)
print(anothor.next.val)
