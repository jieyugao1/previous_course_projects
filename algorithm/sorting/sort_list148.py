# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Insertion sort
# step1: traversing each element of the input linked list
# step2: find the appropriate position to insert the current value
# step3: update the current value and the changed the next link to appropriate ones
# return the result
 
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()  # the linked list to store the result
        while head: 
            prev = result # each iteration, the current result 
            while prev.next and prev.next.val <= head.val:# this is to find the value where
                                                            # we should insert the current head value 
                prev = prev.next 
            h_next = head.next #next head value
            head.next = prev.next # make the next head value to be the prev.next
            prev.next = head # insert head to be the appropriate position.
            head = h_next # update the head value 
        return result.next
