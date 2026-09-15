# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr:
            l.append(curr)
            curr=curr.next
        n=len(l)-n
        curr=dummy=ListNode()
        for i,k in enumerate(l):
            if i==n:
                continue
            curr.next=k
            curr=curr.next
        curr.next=None
        return dummy.next

            
        