class UnionFind:
    def __init__(self, size=10):
        self.id = [i for i in range(size)]
        self.size = size

    def is_valid(self, u):
        return 0 <= u < self.size

    def is_connected(self, u, v):
        if not self.is_valid(u) or not self.is_valid(v):
            return

        return self.id[u] == self.id[v]

    # time O(1)
    # space O(1)

    def union(self, u, v):
        if not self.is_valid(u) or not self.is_valid(v) or self.is_connected(u, v):
            return

        u_id = self.id[u]
        v_id = self.id[v]
        for i in range(self.size):
            if self.id[i] == u_id:
                self.id[i] = v_id

    # time O(n)
    # space O(1)


class QuickFind:
    def __init__(self, size=10):
        self.parent = [i for i in range(size)]
        self.size = size
        self.sizes = [1 for _ in range(size)]

    def is_valid(self, u):
        return 0 <= u < self.size

    def get_root(self, u):
        if not self.is_valid(u):
            return -1

        while u != self.parent[u]:
            # path compression
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]

        return u

    def is_connected(self, u, v):
        if not self.is_valid(u) or not self.is_valid(v):
            return

        return self.get_root(u) == self.get_root(v)

    def union(self, u, v):
        if not self.is_valid(u) or not self.is_valid(v) or self.is_connected(u, v):
            return

        root_u = self.get_root(u)
        root_v = self.get_root(v)

        if self.sizes[root_u] < self.sizes[root_v]:
            self.parent[root_u] = root_v
            self.sizes[root_v] += self.sizes[root_u]
        else:
            self.parent[root_v] = root_u
            self.sizes[root_u] += self.sizes[root_v]
