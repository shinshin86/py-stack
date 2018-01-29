class Stack:
    def __init__(self, max_size=100):
        self.tail = 0
        self.array = [None] * max_size
        self.max_buffer = max_size

    def is_empty(self):
        return self.tail == 0

    def is_full(self):
        return self.tail >= self.max_buffer

    def push(self, data):
        if self.is_full():
            print("--------> Stack is Full!!")
            return False

        self.array[self.tail] = data
        self.tail += 1
        return True

    def pop(self):
        if self.is_empty():
            print("---------> Stack is empty!!")
            return False

        data = self.array[self.tail - 1]
        self.tail -= 1
        return data

    def print_stack_all(self):
        print(self.array[:self.tail])

    def get_stack_all_list(self):
        return self.array[:self.tail]
