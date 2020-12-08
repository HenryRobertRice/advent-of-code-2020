from collections import deque
from re import search
from sys import stdin


class Bag():
    def __init__(self, name):
        self.name = name
        self.contains = []


def main():
    bags = {}
    for line in stdin:
        bag_info = line.strip().split(" bags contain ")
        bag_name = bag_info[0]
        bag_contains = [counts(contained) for contained in bag_info[1].split(", ")]
        if bag_name not in bags:
            bags[bag_name] = Bag(bag_name)
        if bag_contains[0][0] == -1:
            continue
        for contained in bag_contains:
            if contained[1] not in bags:
                bags[contained[1]] = Bag(contained[1])
            bags[bag_name].contains.append([contained[0], bags[contained[1]]])
    print(contains_count(bags["shiny gold"]) - 1)


def counts(contained):
    if contained == "no other bags.":
        return [-1, "n/a"]
    items = contained.split()
    return [int(items[0]), f"{items[1]} {items[2]}"]


def contains_count(bag):
    if bag.contains == []:
        return 1
    return 1 + sum([c[0] * contains_count(c[1]) for c in bag.contains])


if __name__ == "__main__":
    main()
