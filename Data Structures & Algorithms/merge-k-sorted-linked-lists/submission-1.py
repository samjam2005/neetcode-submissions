# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        l = []

        for head in lists:
            curr = head

            while curr:
                l.append(curr)
                curr = curr.next

        if not l:
            return None

        l.sort(key=lambda node: node.val)

        for i in range(len(l) - 1):
            l[i].next = l[i + 1]

        l[-1].next = None

        return l[0]
        
    
        


            

            
        