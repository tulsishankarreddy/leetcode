''' Solution uses 2 pointer method. !st pointer take 1 step at a time 
whereas 2nd pointer takes 2 steps at a time'''


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow