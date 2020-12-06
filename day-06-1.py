from itertools import groupby
from sys import stdin


def main():
    lines = [line.strip() for line in stdin]
    groups = [list(group) for k, group in groupby(lines, lambda l: l == "") if not k]
    answers = [len(set("".join(g))) for g in groups]
    print(sum(answers))


if __name__ == "__main__":
    main()
