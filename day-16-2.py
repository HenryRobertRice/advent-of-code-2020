from sys import stdin


def main():
    your_ticket = False
    nearby_tickets = False
    nearby_ticket_numbers = []
    fields = dict()
    for line in stdin:
        if line == "your ticket:\n":
            your_ticket = True
            continue
        if line == "nearby tickets:\n":
            nearby_tickets = True
            continue
        if your_ticket:
            your_ticket_numbers = line.strip().split(",")
            your_ticket = False
            continue
        if nearby_tickets:
            nearby_ticket_numbers.append(line.strip().split(","))
            continue
        if line != "\n":
            parts1 = line.strip().split(":")
            name = parts1[0]
            parts2 = parts1[1].strip().split()
            values1 = parts2[0].split("-")
            values2 = parts2[2].split("-")
            fields[name] = [values1[0], values1[1], values2[0], values2[1]]
    valid_tickets = [t for t in nearby_ticket_numbers if is_valid_ticket(t, fields)]
    if is_valid_ticket(your_ticket_numbers, fields):
        valid_tickets.append(your_ticket_numbers)
    fields_deciphered = {name: find_valid_positions(fields[name], valid_tickets) for name in fields}
    while not is_refined(fields_deciphered):
        refine(fields_deciphered)
    for f in fields_deciphered:
        fields_deciphered[f] = fields_deciphered[f].index(True)
    result = 1
    for f in fields_deciphered:
        if "departure" in f:
            result *= int(your_ticket_numbers[fields_deciphered[f]])
    print(result)


def refine(fields_deciphered):
    solved = [f for f in fields_deciphered if fields_deciphered[f].count(True) == 1]
    for s in solved:
        i = fields_deciphered[s].index(True)
        for f in fields_deciphered:
            if f != s:
                fields_deciphered[f][i] = False


def is_refined(fields_deciphered):
    for f in fields_deciphered:
        if fields_deciphered[f].count(True) > 1:
            return False
    return True


def find_valid_positions(field, tickets):
    validities = [True for _ in range(len(tickets[0]))]
    for i in range(len(validities)):
        if not is_valid_position(field, tickets, i):
            validities[i] = False
    return validities


def is_valid_position(field, tickets, position):
    for i in range(len(tickets)):
        val = int(tickets[i][position])
        f = list(map(int, field))
        if not (f[0] <= val <= f[1] or f[2] <= val <= f[3]):
            return False
    return True


def is_valid_ticket(ticket, fields):
    for n in ticket:
        n = int(n)
        valid = False
        for f in fields:
            nums = list(map(int, fields[f]))
            if nums[0] <= n <= nums[1] or nums[2] <= n <= nums[3]:
                valid = True
                break
        if not valid:
            return False
    return True


if __name__ == "__main__":
    main()
