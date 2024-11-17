from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#   newList = list1 + list2
#   n = len(newList)
#   i = 0
#   while i < n:
#     j = i+1
#     while j < n:
#         if newList[i] > newList[j]:
#            newList[i], newList[j] = newList[j], newList[i]
#         j += 1
#     i += 1
#   return newList
# print(mergeTwoLists([1,2,4],[1,3,4]))

# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
#     def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # Base cases: if one of the lists is empty, return the other list
#         if not list1:
#             return list2
#         if not list2:
#             return list1

#         # Compare the values of the current nodes
#         if list1.val < list2.val:
#             # If list1 has a smaller value, move to the next node in list1
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             # If list2 has a smaller or equal value, move to the next node in list2
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2
        
    # print(mergeTwoLists2([1,2,4],[1,3,4]))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        # Return the head of the merged list (skip the dummy node)
        return dummy.next
# Create ListNode objects for the input lists
list1Ex = ListNode(1, ListNode(2, ListNode(4)))
list2Ex = ListNode(1, ListNode(3, ListNode(4)))

# Create an instance of Solution class
solution = Solution()
# Call the mergeTwoLists method
merged_list = solution.mergeTwoLists(list1Ex, list2Ex)
# Print the merged list
while merged_list:
  print(merged_list.val, end=" -> ")
  merged_list = merged_list.next
