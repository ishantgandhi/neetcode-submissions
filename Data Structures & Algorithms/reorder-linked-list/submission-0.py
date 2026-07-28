# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        prev = slow.next = None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first = head
        second = prev
        while second:
            fnxt,snxt = first.next, second.next
            first.next = second
            second.next = fnxt
            first = fnxt
            second = snxt
        

        

