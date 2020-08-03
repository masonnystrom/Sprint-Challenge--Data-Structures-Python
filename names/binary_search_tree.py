# from queue import Queue
# from stack import Stack
from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare input value with value of the node
        # if the value is < Node's value
        if value < self.value:
            # we need to go left
            # if there's no node to compare the input value tok
            if self.left == None:
                # we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
            # call the left child's insert method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go right, but let's see if we see there is no right child
            if self.right == None:
            # then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
            # call right child's insert method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        # check left side
        elif target < self.value and self.left:
            return self.left.contains(target)
        # check right side
        elif target > self.value and self.right:
            return self.right.contains(target)
        else:
            return None

    # Return the maximum value found in the tree
    def get_max(self):
        """max value will be the right most value"""
        # recuriseve go right until you can't go right
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # apply to root node
        fn(self.value)
        # recursively apply fn to left nodes
        if self.left:
            self.left.for_each(fn)
        # recursively apply fn to righ tnodes
        if self.right:
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self,fn):
        # Depth first: LIFO
        # use a stack to traverse the tree and add nodes
        stack = []
        stack.append(self) # append root node

        while len(stack) > 0:
            current = stack.pop()
            # add current node's right child first
            if current.right:
                stack.append(current.stack)

            if current.left:
                stack.append(current.left)

            fn(current.value)


    def iterative_breadth_first_for_each(self,fn):
        # more like a cue, FIFO
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        fn(current.value)

# Part 2 -----------------------

# Print all the values in order from low to high
# Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def dft_print(self, node):
        """ depth first traversal explores the entire length of a branch on a tree, retreats then does the same thing on the first unexplored branch."""
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def bft_print(self, node):
        """bredth first traversal explores all nodes on a given layer, adds those nodes to a queue, then explores the next layer"""
        #1. define deque
        #2. add self to deque
        #3. iterate: while there are items in the deque 
        #4. dequeue/pop from deque, point to result, and print
        #5. add left and right children to deque

        que = Queue()
        que.enqueue(self)
        while len(que) > 0:
            current = que.dequeue()
            print(current.value)
            if current.left:
                que.enqueue(current.left)
            if current.right:
                que.enqueue(current.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        '''node the list of data objects so far in the traversal'''
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # # Print Post-order recursive DFT
    def post_order_dft(self, node):
        """Node is the list of values so far in the traversal """
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)

# """This code is necessary for testing the `print` methods"""

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
