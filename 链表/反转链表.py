"""
https://leetcode.cn/problems/reverse-linked-list/solutions/562122/shi-pin-jiang-jie-die-dai-he-di-gui-hen-hswxy/
"""

# 1. 迭代解法
def reverseList(head):
    prev,curr = None,head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# 2. 递归解法
def reverseList2(head):
    if head is None or head.next is None:
        return head
    p = reverseList2(head.next)
    head.next.next = head
    head.next = None
    return p