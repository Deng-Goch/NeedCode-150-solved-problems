# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ## O(n)
    def hasCycle(self, head):
        curr = head
        while curr:
            if curr.val == 'visted':
                return True
            else:
                curr.val = 'visted'
                curr = curr.next
        return False


if __name__ == "__main__":

    y = ListNode(1)
    a = y.next = ListNode(2)
    b = y.next.next = ListNode(3)
    c = y.next.next.next = ListNode(2)
    # c.next = a

    x = Solution()
    print(x.hasCycle(y))