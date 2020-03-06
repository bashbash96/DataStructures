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
