import unittest
from stack import Stack


class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_initialize_stack_buffer(self):
        self.assertTrue(len(self.s.array) == 100)
        self.assertTrue(self.s.max_buffer == 100)

    def test_initialize_stack_change_buffer_size(self):
        s = Stack(10)
        self.assertTrue(len(s.array) == 10)
        self.assertTrue(s.max_buffer == 10)

    def test_is_full(self):
        for i in range(100):
            self.s.push(i)
        self.assertFalse(self.s.push("test"))

    def test_is_empty(self):
        self.assertFalse(self.s.pop())

    def test_push(self):
        self.s.push("test1")
        self.s.push("test2")
        self.s.push("test3")
        stack_list = self.s.get_stack_all_list()
        self.assertTrue(stack_list[0] == "test1")
        self.assertTrue(stack_list[1] == "test2")
        self.assertTrue(stack_list[2] == "test3")
        self.assertTrue(len(stack_list) == 3)
        self.assertTrue(self.s.tail == 3)

    def test_pop(self):
        self.s.push("test1")
        self.s.push("test2")
        self.s.push("test3")
        self.assertTrue(self.s.pop() == "test3")
        self.assertTrue(len(self.s.get_stack_all_list()) == 2)
        self.assertTrue(self.s.tail == 2)

    def test_get_stack_all_list(self):
        self.s.push("test1")
        self.s.push("test2")
        check_list = ["test1", "test2"]
        self.assertTrue(len(self.s.get_stack_all_list()) == 2)
        self.assertTrue(self.s.get_stack_all_list() == check_list)
