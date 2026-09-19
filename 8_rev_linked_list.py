# Definition for singly-linked list.
class ListNode:
      def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

## O(n)
class Solution:
    def reverseList(self, head):
        stack = list([])

        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        
        while curr:
            curr.val = stack[-1]
            stack.pop()
            curr = curr.next
        return head


if __name__ == "__main__":
    x = ListNode(1)
    x.next = ListNode(2)
    x.next.next = ListNode(3)
    x.next.next.next = ListNode(4)
    x.next.next.next.next = ListNode(5)
    x.next.next.next.next.next = ListNode(6)

    print("\n")

    def show(head):
        while head:
            print(head.val)
            head = head.next
        return
    

    show(x)

    y = Solution()
    y.reverseList(x)


    print("\n")

    show(x)