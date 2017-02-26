import unittest
from add_two_numbers import *


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @staticmethod
    def gen_list(*args):
        list_nodes = []
        for num in args:
            list_nodes.append(ListNode(num))
        for i in range(len(list_nodes - 1)):
            list_nodes[i].next = list_nodes[i + 1]
        return list_nodes[0]

    @staticmethod
    def compare_list(l1, l2):
        while l1 is not None and l2 is not None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None

    def testTwoSum(self):
        a0 = ListNode(2)
        a1 = ListNode(3)
        a2 = ListNode(4)
        a0.next = a1
        a1.next = a2
        self.assertEqual(
            self.compare_list(self.solution.addTwoNumbers(self.gen_list(2, 4, 3),
                                                          self.gen_list(5, 6, 4)), self.gen_list(7, 0, 8)),
            True, "test failed")
        self.assertEqual(
            self.compare_list(self.solution.addTwoNumbers(self.gen_list(2, 4, 3, 2),
                                                          self.gen_list(5, 6, 4)), self.gen_list(7, 0, 8, 2)),
            True, "test failed")

    if __name__ == '__main__':
        unittest.main()
