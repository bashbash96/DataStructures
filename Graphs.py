# ----------------- Graph implementation with list ---------------------

from sys import maxsize
from collections import defaultdict


class Graph:
    def __init__(self):
        """
        constructor for graph
        """
        self.E = defaultdict(set)
        self.v = set()

    def addEdge(self, u, v):
        """
        add new edge between two vertices (u,v), for undirected graph remove
        the commented instructions
        :param u:
        :param v:
        :return:
        """
        self.v.add(v)
        self.v.add(u)

        if u in self.E:
            self.E[u].add(v)
        else:
            self.E[u] = {v}

        # if v in self.E:
        #     self.E[v].add(u)
        # else:
        #     self.E[v] = {u}

    def BFS(self, v):
        """
        Breadth-First Search traversal on graph
        :param v:
        :return:
        """
        # initialization
        distance = {}
        color = {}
        parent = {}

        for ver in self.v:
            distance[ver] = maxsize
            color[ver] = 'w'
            parent[ver] = None

        distance[v] = 0
        color[v] = 'g'

        # creating a queue
        q = [v]

        while len(q) > 0:
            curr = q.pop(0)
            print(curr, end=' ')

            # for all adjacent nodes if there is an adjacent node that we didn't visit, visit it
            for ver in self.E[curr]:
                if color[ver] == 'w':
                    color[ver] = 'g'
                    distance[ver] = distance[curr] + 1
                    parent[ver] = curr
                    q.append(ver)

            color[curr] = 'b'

        print()

        return distance, parent

        # time O(|V| + |E|)
        # space O(|V|)

    def printPath2(self, u, v, parent):
        if u == v:
            print(v, end=' ')
        else:
            if parent[v] is None:
                print('no path')
            else:
                self.printPath2(u, parent[v], parent)
                print(v, end=' ')

    def printPath(self, u, v):
        (d, f) = self.BFS(u)

        self.printPath2(u, v, f)

        # time O(|E|)
        # space O(|E|)

    def DFS(self):
        color, parent = {}, {}

        for v in self.v:
            color[v] = 'w'
            parent[v] = None

        for v in self.v:
            if color[v] == 'w':
                self.DFSVisit(v, color, parent)

        return parent

        # time O(|V| + |E|)
        # space O(|V|)

    def DFSVisit(self, u, color, parent):
        color[u] = 'g'
        print(u, end=' ')
        for v in self.E[u]:
            if color[v] == 'w':
                parent[v] = u
                self.DFSVisit(v, color, parent)

        color[u] = 'b'

    def TopologicalSort(self):
        color = {}
        ans = []

        if self.isCyclic():
            return 'Error - can\'t do a topological sort for cyclic graph'
        for v in self.v:
            color[v] = 'w'

        for v in self.v:
            if color[v] == 'w':
                self.topologicalVisit(v, color, ans)

        ans.reverse()
        print(ans)

        # time O(|V| + |E|)
        # space O(|V| + |E|)

    def topologicalVisit(self, u, color, ans):
        color[u] = 'g'

        for v in self.E[u]:
            if color[v] == 'w':
                self.topologicalVisit(v, color, ans)

        color[u] = 'b'
        ans.append(u)

    def isCyclic(self):
        color = {}

        for v in self.v:
            color[v] = 'w'

        for v in self.v:
            if self.isCyclic2(v, color):
                return True

        return False

        # time O(|V| + |E|)
        # space O(|V| )

    def isCyclic2(self, v, color):
        color[v] = 'g'

        for u in self.E[v]:
            if color[u] == 'w':
                self.isCyclic2(u, color)
            elif color[u] == 'g':
                return True

        color[v] = 'b'
        return False