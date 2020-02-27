import sys
# from dll_stack import Stack
# from dll_queue import Queue
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                    return
                self.left = BinarySearchTree(value)
                return
            if self.right:
                self.right.insert(value)
                return
            self.right = BinarySearchTree(value)
            return
        self.value = value

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        """
        Angry Linter
        """
        if self.value:
            if target == self.value:
                return True
            if target <= self.value and self.left:
                return self.left.contains(target)
            if target >= self.value and self.right:
                return self.right.contains(target)
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        if self.value <= self.right.value:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


D = BinarySearchTree(5)
D.insert(6)
D.insert(6)
D.insert(6)
D.insert(2)
D.insert(2)
D.insert(2)
D.insert(7)
print(D.get_max())
