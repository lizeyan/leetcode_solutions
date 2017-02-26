# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_nodes = []
        while l1 is not None and l2 is not None:
            list_nodes.append(ListNode(l1.val + l2.val))
            l1 = l1.next
            l2 = l2.next
        if l1 is not None:
            ptr = l1
        elif l2 is not None:
            ptr = l2
        else:
            ptr = None
        while ptr is not None:
            list_nodes.append(ListNode(ptr.val))
            ptr = ptr.next
        for i in range(len(list_nodes) - 1):
            list_nodes[i + 1].val += int(list_nodes[i].val / 10)
            list_nodes[i].val %= 10
            list_nodes[i].next = list_nodes[i + 1]
        if list_nodes[-1].val >= 10:
            list_nodes[-1].next = ListNode(int(list_nodes[-1].val / 10))
            list_nodes[-1].val %= 10
        return list_nodes[0]
