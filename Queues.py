# ------------------- Queue implementation with Linked List ------------------
class Node:
    def __init__(self, data):
        """
        constructor of a node
        :param data: data of the node
        """
        self.data = data
        self.next = None


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
        node = Node(data)
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
        if not self.head:
            return None

        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None

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


class CircularQueue:
    def __init__(self, capacity):
        self.queue = [-1] * capacity
        self.size = 0
        self.capacity = capacity
        self.head = 0
        self.tail = -1

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.size += 1
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value

        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.queue[self.head] = -1
        self.size -= 1
        self.head = (self.head + 1) % self.capacity

        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self):
        """
        :rtype: bool
        """

        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """

        return self.size == self.capacity


"""
    [-1, 2, 3]
            t
         h 
"""
