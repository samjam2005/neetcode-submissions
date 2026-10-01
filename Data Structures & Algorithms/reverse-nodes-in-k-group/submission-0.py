class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        curr = head
        l = []
        j = []

        while curr:
            j.append(curr)
            curr = curr.next

            if len(j) == k:
                j.reverse()
                l += j
                j = []

        # leftover nodes stay in original order
        l += j

        for i in range(len(l) - 1):
            l[i].next = l[i + 1]

        if l:
            l[-1].next = None
            return l[0]

        return None