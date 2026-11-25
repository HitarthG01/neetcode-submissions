# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head
        rep_list = []
        count = 0

        while curr:
            rep_list.append(curr)
            curr = curr.next

            for num in range(0, len(rep_list)):
                if curr in rep_list:
                    return True

            count = count + 1
        return False
