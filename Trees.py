import sys


# ------------------- Linked List Trees ------------------
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None


# ------------------- Queue implementation with Linked List ------------------
class Queue:
    def __init__(self):
        """
        constructor of empty Queue
        """
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        """
        add new node to the queue
        :param data: data to insert
        :return:
        """
        node = Node2(data)
        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def dequeue(self):
        """
        remove the first element of the queue
        :return: data / None
        """
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data

    def isEmpty(self):
        """
        check if the queue is empty or note
        :return: True / False
        """
        return self.length == 0

    def deleteQueue(self):
        """
        delete the entire queue
        :return:
        """
        self.head = self.tail = None

    def peek(self):
        """
        :return: the data of the head node
        """
        if self.head:
            return self.head.data

        return None

    def printQueue(self):
        """
        print the queue elements
        :return:
        """
        curr = self.head

        while curr.next is not None:
            print(curr.data, end=" -> ")
            curr = curr.next

        if curr is not None:
            print(curr.data)


# ------------------- Binary Search Tree implementation with Linked List ------------------
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert2(self.root, data)

    def insert2(self, node, data):

        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert2(node.right, data)
        else:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert2(node.left, data)

    # ------------------- DFS Traversal ------------------
    def inOrder(self):
        """
        in order traversal to a binary tree
        :return:
        """
        self.inOrder2(self.root)
        print()

    def inOrder2(self, node):
        if node is None:
            return

        self.inOrder2(node.left)
        print(node.data, end=" ")
        self.inOrder2(node.right)

    def preOrder(self):
        """
        pre order traversal to a binary tree
        :return:
        """
        self.preOrder2(self.root)
        print()

    def preOrder2(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self.preOrder2(node.left)
        self.preOrder2(node.right)

    def postOrder(self):
        """
         post order traversal to a binary tree
        :return:
        """
        self.postOrder2(self.root)
        print()

    def postOrder2(self, node):
        if node is None:
            return

        self.postOrder2(node.left)
        self.postOrder2(node.right)
        print(node.data, end=" ")

    # ------------------- BFS Traversal ------------------
    def BFS(self):
        if self.root is None:
            return

        q = Queue()
        q.enqueue(self.root)
        while q.length > 0:
            curr = q.dequeue()
            print(curr.data, end=" ")
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

        print()

    def height(self):
        return self.height2(self.root)

    def height2(self, node):
        if node is None:
            return 0

        return 1 + max(self.height2(node.left), self.height2(node.right))

