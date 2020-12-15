from itertools import product
from sys import stdin


def main():
    mask = dict()
    mem = dict()
    instructions = [line.split() for line in stdin]
    for i in instructions:
        if i[0] == "mask":
            mask = i[2]
        else:
            addr = bin(int(i[0][4:-1]))[2:]
            val = int(i[2])
            masked_addrs = apply_mask(mask, addr)
            for m in masked_addrs:
                mem["".join(m)] = val
    print(sum(mem.values()))


def apply_mask(mask, addr):
    masked_addr = ["0" for _ in range(36)]
    j = 0
    for i in range(len(masked_addr) - len(addr), len(masked_addr)):
        masked_addr[i] = addr[j]
        j += 1
    for i in range(len(mask)):
        if mask[i] != "0":
            masked_addr[i] = mask[i]
    return expand_floating_bits(masked_addr)


def expand_floating_bits(masked_addr):
    floating_bits = [i for i in range(len(masked_addr)) if masked_addr[i] == "X"]
    resolved_bits = product(["0", "1"], repeat=len(floating_bits))
    expanded = [assign_bits(masked_addr, floating_bits, r) for r in resolved_bits]
    return expanded


def assign_bits(masked_addr, floating_bits, resolved_bits):
    copy = masked_addr[:]
    for i in range(len(floating_bits)):
        copy[floating_bits[i]] = resolved_bits[i]
    return copy

if __name__ == "__main__":
    main()
