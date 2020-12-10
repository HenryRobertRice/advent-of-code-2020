from sys import stdin


def main():
    corrupted = [line.strip().split() for line in stdin]
    fixed = generate_fixed(corrupted)
    for fix in fixed:
        i = 0
        acc = 0
        executed = set()
        while i not in executed:
            if i >= len(fix):
                print(acc)
                return
            executed.add(i)
            i, acc = execute(i, acc, fix[i])


def generate_fixed(corrupted):
    fixed = []
    for i in range(len(corrupted)):
        if corrupted[i][0] in ["jmp", "nop"]:
            new_instruction = ["nop" if corrupted[i][0] == "jmp" else "jmp", corrupted[i][1]]
            fix = corrupted[:]
            fix[i] = new_instruction
            fixed.append(fix)
    return fixed


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
