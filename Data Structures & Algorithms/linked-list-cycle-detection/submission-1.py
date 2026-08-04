# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        trav = head
        while trav:
            if trav:
                if trav in seen:
                    return True
                else:
                    seen.add(trav)
            trav = trav.next
            
        return False

