# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    copy = head
    array = []
    while copy:
      array.append(copy)
      copy = copy.next
    m = array[len(array) // 2]
    while head:
      if head == m:
        return head  
      head = head.next

list1 = ListNode(1, ListNode(2, ListNode(3,  ListNode(4,  ListNode(5)))))
solution = Solution()
ans = solution.middleNode(list1)
while ans:
  print(ans.val, end=" -> ")
  ans = ans.next