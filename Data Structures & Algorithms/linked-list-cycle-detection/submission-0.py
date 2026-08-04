# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        seen.add(head)
        trav = head
        while trav:
            trav = trav.next
            if trav and trav in seen:
                return True
            elif trav:
                seen.add(trav)
        return False

