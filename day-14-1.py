from sys import stdin


def main():
    mask = dict()
    mem = dict()
    instructions = [line.split() for line in stdin]
    for i in instructions:
        if i[0] == "mask":
            mask = new_mask(i[2])
        else:
            addr = int(i[0][4:-1])
            val = bin(int(i[2]))[2:]
            mem[addr] = apply_mask(mask, val)
    print(sum(mem.values()))


def new_mask(mask):
    return {i: m for (i, m) in enumerate(mask) if m in ["0", "1"]}


def apply_mask(mask, value):
    result = ["0" for _ in range(36)]
    j = 0
    for i in range(len(result) - len(value), len(result)):
        result[i] = value[j]
        j += 1
    for m in mask:
        result[m] = mask[m]
    return int("".join(result), 2)


if __name__ == "__main__":
    main()
