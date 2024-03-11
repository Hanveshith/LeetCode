# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        st = [head.val]
        while(temp):
            if(temp.val < st[-1]):
                st.append(temp.val)
            else:
                while(st and st[-1] < temp.val):
                    st.pop()
                st.append(temp.val)
            temp = temp.next
        dummy = ListNode()
        curr = dummy
        for i in st:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next