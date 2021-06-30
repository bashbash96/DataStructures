from Queues import Queue


# ------------------- Linked List Trees ------------------
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


# ------------------- Trie implementation with hashMap ------------------

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]

        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root

        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        else:
            return True


# ------------------- Binary Search Tree implementation with Linked List ------------------
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if not node:
            return Node(data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        else:
            node.left = self._insert(node.left, data)

        return node

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            return None
        if data > node.data:
            node.right = self._delete(node.right, data)
        elif data < node.data:
            node.left = self._delete(node.left, data)
        else:
            # one or no children
            if not node.left:
                return node.right

            if not node.right:
                return node.left

            # two children

            successor = BST._min(node.right)

            node.data = successor
            node.right = self._delete(node.right, successor)

        return node

    @staticmethod
    def _min(node):
        curr = node
        min_val = node.data
        while curr:
            min_val = curr.data
            curr = curr.left

        return min_val

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
