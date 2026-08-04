# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # list of length 0 or 1
        if head == None or head.next == None:
            return

        st = []
        trav = head
        n = 0 # length of list
        while trav != None:
            st.append(trav)
            trav = trav.next
            n += 1

        add_from_stack = True
        i = 1
        trav = head
        nxt = head.next

        while i < n:
            if add_from_stack:
                top = st.pop() # should be fine to call bc never going to get past half
                trav.next = top
            elif nxt:
                trav.next = nxt
                nxt = nxt.next
            add_from_stack ^= True # light switch!
            i += 1
            trav = trav.next

        trav.next = None


            

        
        
        