class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
class Solution:
    '''def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count'''
    def addTwoNumbers(self, l1, l2):
        l3=ListNode()
        current=l3
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            total=v1+v2+carry
            carry,rem=divmod(total,10)
            current.next=ListNode(rem)
            current=current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return l3.next