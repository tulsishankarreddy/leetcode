''' Solution uses 2 pointers. Since n is given from end of the linked llist, the fast pointer should be n steps
ahead of slow pointer. Once fast pointer reaches end of the linked list, slow pointer would have reached the
desired node which has ro be removed'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None:
            return None        
        
        fast, slow = head, head
        
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        if n == 1:
            slow.next = None
            
        else:
            slow.next = slow.next.next
            
        return head