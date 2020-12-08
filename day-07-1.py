from collections import deque
from re import search
from sys import stdin


class Bag():
    def __init__(self, name):
        self.name = name
        self.contained_by = []


def main():
    bags = {}
    for line in stdin:
        bag_info = line.strip().split(" bags contain ")
        bag_name = bag_info[0]
        bag_contains = [search("[a-z]+ [a-z]+", contained).group(0) for contained in bag_info[1].split(", ")]
        if bag_name not in bags:
            bags[bag_name] = Bag(bag_name)
        if bag_contains[0] == "no other":
            continue
        for contained in bag_contains:
            if contained not in bags:
                bags[contained] = Bag(contained)
            bags[contained].contained_by.append(bags[bag_name])
    print(shiny_gold_search(bags["shiny gold"]))


def shiny_gold_search(bag):
    q = deque([bag])
    seen = set(["shiny gold"])
    can_contain = -1
    while q:
        visiting = q.popleft()
        can_contain += 1
        for container in visiting.contained_by:
            if container.name not in seen:
                q.append(container)
                seen.add(container.name)
    return can_contain


if __name__ == "__main__":
    main()
