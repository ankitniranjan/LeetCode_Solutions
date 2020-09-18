# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = None

class Solution:
    def to_int(l: ListNode):		l: LinkNode => Typecasting
        s = ''
        while l != None:
            s += str(l.val)
            l = l.next
        return int(s[::-1])     #Returning reversed version
    
    def to_list(n: int):
        s = str(n)[::-1]    #Reversing, for inserting purpose
        head = None
        for ch in s:
            node = ListNode(int(ch))  
            if head is None:
                head = node
            else:
                temp = head
                while temp.next is not None:
                    temp = temp.next
                temp.next = node
        return head
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = Solution.to_int(l1)
        b = Solution.to_int(l2)
        return Solution.to_list(a + b)
