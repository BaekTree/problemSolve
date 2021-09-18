#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        
            given n.
            get the length of the...
                we cannot get the length until we see the end node.
                
                space complexity 2n
                
                keep the n nodes always.
                if rechead to the end, move the nth one. 
                link n-1 and n+1.
                
                every iteration, change the sub_head. change the sub_tail.
                

                
                what if the temp length is not yet become n?
                    sub_len = 1
                    sub_head = head
                    
                # update temp linked list
                
                
                
                    
            
            denotation
                head: main linked list head.
                sub_head: the temporary linked list head.
                sub_tail: the temporary linked list tail.
                
        """
        
        cur_node = sub_head = sub_tail = head
        sub_len = 1
        
        while cur_node.next:
            cur_node = cur_node.next

            sub_len += 1
            if sub_len > n + 1:
                sub_head = sub_head.next
            sub_tail = sub_tail.next
        if sub_head == sub_tail:
            return None

        if sub_len == n:
            return head.next
        sub_head.next = sub_head.next.next
        return head

