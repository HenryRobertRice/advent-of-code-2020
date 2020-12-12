from collections import deque
from sys import stdin


class Node():
    def __init__(self, state):
        self.state = state
        self.paths = 0
        self.next_ = []
        self.prev = []


def main():
    adapters = [int(line) for line in stdin]
    adapters.sort()
    nums = tuple([0] + adapters + [adapters[-1] + 3])
    nodes = {nums: Node(nums)}
    seen = set()
    q = deque([nums])
    while q:
        visiting = q.popleft()
        seen.add(visiting)
        start = visiting[0]
        for i in range(1, min(4, len(visiting))):
            if 1 <= visiting[i] - start <= 3:
                next_ = visiting[i:]
                if next_ not in seen:
                    seen.add(next_)
                    q.append(next_)
                    nodes[next_] = Node(next_)
                nodes[visiting].next_.append(nodes[next_])
                nodes[next_].prev.append(nodes[visiting])
    nodes[nums].paths = 1
    print(count_paths(nodes[nums]))


def count_paths(node):
    total_paths = 0
    seen = set()
    q = deque([node])
    while q:
        visiting = q.popleft()
        if visiting.paths > total_paths:
            total_paths = visiting.paths
        for n in visiting.next_:
            n.paths += visiting.paths
            if n not in seen:
                seen.add(n)
                q.append(n)
    return total_paths


if __name__ == "__main__":
    main()
