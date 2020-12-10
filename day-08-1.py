from sys import stdin


def main():
    instructions = [line.strip().split() for line in stdin]
    i = 0
    acc = 0
    executed = set()
    while i not in executed:
        executed.add(i)
        i, acc = execute(i, acc, instructions[i])
    print(acc)


def execute(i, acc, instruction):
    if instruction[0] == "acc":
        acc += int(instruction[1])
        i += 1
    elif instruction[0] == "jmp":
        i += int(instruction[1])
    elif instruction[0] == "nop":
        i += 1
    return i, acc


if __name__ == "__main__":
    main()
