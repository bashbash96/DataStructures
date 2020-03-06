# ------------------- Stack implementation with Linked List ------------------
class Node:
    def __init__(self, data):
        """
        constructor of a node
        :param data: data of the node
        """
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        """
        constructor of empty stack
        """
        self.head = None
        self.size = 0

    def push(self, data):
        """
        add new node to head of the stack
        :param data:
        :return:
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        """
        remove node from the head of the stack
        :return: data of the removed node
        """
        data = None

        if self.head:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1

        return data

    def length(self):
        """
        :return: the length of the stack
        """
        return self.size

    def isEmpty(self):
        """
        check if the stack empty or not
        :return: True / False
        """
        return self.size == 0

    def peek(self):
        """
        :return: the data of the head node
        """
        if self.head:
            return self.head.data

    def deleteStack(self):
        """
        delete the entire stack
        :return:
        """
        self.head = None

    def printStack(self):
        """
        print the stack elements
        :return:
        """
        if not self.head:
            return

        curr = self.head
        while curr.next:
            print(curr.data, end=" -> ")
            curr = curr.next

        if curr:
            print(curr.data)
