from sys import stdin, exit
from pprint import pprint


class Node:
    def __init__(self, exp, _id):
        self.exp = exp[1 : len(exp) - 1] if all_in_parens(exp) else exp
        self._id = _id
        self.children = []


def all_in_parens(exp):
    if exp[0] == "(" and exp[-1] == ")":
        parens_depth = 1
        for j in range(1, len(exp) - 1):
            if exp[j] == "(":
                parens_depth += 1
            if exp[j] == ")":
                if parens_depth == 1:
                    return False
                parens_depth -= 1
        return True


def main():
    expressions = [line.replace(" ", "").strip() for line in stdin]
    print(sum([evaluate(exp) for exp in expressions]))


def evaluate(expression):
    tree = make_tree(expression)
    flatten_tree(tree)
    return int(tree[1].exp)


def make_tree(expression):
    nodes = {1: Node(expression, 1)}
    while not_done(nodes):
        break_leafs(nodes)
    return nodes


def break_leafs(nodes):
    for i in list(nodes):
        n = nodes[i]
        if n.exp.count("+") + n.exp.count("*") > 0 and len(n.exp) > 1:
            parens_depth = 0
            for j in range(len(n.exp) - 1, -1, -1):
                if n.exp[j] == "(":
                    parens_depth += 1
                if n.exp[j] == ")":
                    parens_depth -= 1
                if n.exp[j] in ["+", "*"] and parens_depth == 0:
                    index = j
                    break
            n.children.extend([n._id * 2, n._id * 2 + 1])
            nodes[n._id * 2] = Node(n.exp[:j], n._id * 2)
            nodes[n._id * 2 + 1] = Node(n.exp[j + 1 :], n._id * 2 + 1)
            n.exp = n.exp[j]


def flatten_tree(nodes):
    while len(nodes) > 1:
        trim_leafs(nodes)


def trim_leafs(nodes):
    for i in list(nodes):
        if i in nodes:
            n = nodes[i]
            if is_semiterminal(nodes, n):
                c = n.children
                c0 = nodes[c[0]]
                c1 = nodes[c[1]]
                value = str(
                    int(c0.exp) + int(c1.exp)
                    if n.exp == "+"
                    else int(c0.exp) * int(c1.exp)
                )
                n.exp = value
                del nodes[c[0]]
                del nodes[c[1]]
                n.children = []


def is_semiterminal(nodes, n):
    if len(n.children) != 2:
        return False
    for c in n.children:
        if "+" in nodes[c].exp or "*" in nodes[c].exp:
            return False
    return n.exp == "+" or n.exp == "*"


def not_done(nodes):
    for i in nodes:
        n = nodes[i]
        if n.exp.count("+") + n.exp.count("*") > 0 and len(n.exp) > 1:
            return True
    return False


if __name__ == "__main__":
    main()


"""
turn each expression into a tree
start with one root node for the original expression
until the tree is done:
    break up each leaf node
to break up a leaf node:
    if the whole expression is in parenthesis, remove them
    find the first operator not in parenthesis
    everything to the left/right goes in new child nodes
    the node is now just the operator
"""
