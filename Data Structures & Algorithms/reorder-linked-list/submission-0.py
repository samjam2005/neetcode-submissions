# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l=[]
        curr=head
        while curr:
            l.append(curr)
            curr=curr.next
        curr=l[0]
        count=1
        for i in range(len(l)-1):
            if i%2==0:
                curr.next=l[len(l)-1- (i//2)]
            else:
                curr.next=l[(i+1) //2]
            curr=curr.next
        curr.next=None


