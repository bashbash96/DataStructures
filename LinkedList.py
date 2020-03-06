class Node:
    def __init__(self, data):
        """
        constructor of node
        :param data: data of the node
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        constructor of singly linked list
        """
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):
        """
        add to the beginning of the list
        :param data: data to add
        :return:
        """
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    def append(self, data):
        """
        add to end of the list
        :param data: data to add
        :return:
        """
        newNode = Node(data)

        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

    def size(self):
        """

        :return: the length of the linked list
        """
        return self.length

    def search(self, data):
        """
        check if certain data is in the linked list
        :param data: data to check
        :return: True/False
        """
        curr = self.head

        while curr is not None:
            if curr.data == data:
                return True
            curr = curr.next

        return False

    def delete(self, data):
        """
        remove certain data from the linked list, it will remove
        the first appearance of the data, if there is no such a data
        the function won't do anything
        :param data: data to remove
        :return:
        """
        if self.head is None:
            return

        if self.head.data == data:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
            return

        curr = self.head
        while curr.next is not None:
            if curr.next.data == data:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                self.length -= 1
                return
            curr = curr.next

    def deleteLinkedList(self):
        """
        delete the whole linked list
        :return:
        """
        self.head = self.tail = None

    def printLinkedList(self):
        """
        print the linked list elements
        :return:
        """

        if self.head is None:
            return

        curr = self.head

        while curr.next is not None:
            print(curr.data, "-> ", end='')
            curr = curr.next

        print(curr.data)
