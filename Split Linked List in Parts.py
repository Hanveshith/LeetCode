class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        res = []
        curr = head
        for i in range(k):
            dummy = write = ListNode()
            for j in range(width + (i<remainder)):
                if(curr):
                    write.next = write = ListNode(curr.val)
                    curr = curr.next

            res.append(dummy.next)
        return res