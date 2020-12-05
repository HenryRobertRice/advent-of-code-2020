from sys import stdin


def main():
    print(sum([int(is_valid(line)) for line in stdin]))


def is_valid(line):
    parts = line.split()
    i1, i2 = map(int_decrement, parts[0].split("-"))
    char = parts[1][0]
    password = parts[2]
    return int((password[i1] == char) != (password[i2] == char))


def int_decrement(n):
    return int(n) - 1


if __name__ == "__main__":
    main()
