from itertools import groupby
from string import ascii_lowercase
from sys import stdin


def main():
    lines = [line.strip() for line in stdin]
    groups = [list(group) for k, group in groupby(lines, lambda l: l == "") if not k]
    answers = [get_answers(g) for g in groups]
    print(sum(answers))


def get_answers(group):
    individual_answers = [set(g) for g in group]
    # definitely the weirdest variable name i've ever used
    unanimities = [int(is_unanimous(char, individual_answers)) for char in ascii_lowercase]
    return sum(unanimities)


def is_unanimous(answer, individual_answers):
    unanimous = True
    for i in individual_answers:
        if answer not in i:
            unanimous = False
            break
    return unanimous


if __name__ == "__main__":
    main()
