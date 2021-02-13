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
    error_rate = 0
    abs_error = 0
    for nt in nearby_ticket_numbers:
        for n in nt:
            n = int(n)
            valid = False
            for f in fields:
                nums = list(map(int, fields[f]))
                if nums[0] <= n <= nums[1] or nums[2] <= n <= nums[3]:
                    valid = True
                    break
            if not valid:
                error_rate += n
                abs_error += 1
                break
    print(error_rate)


if __name__ == "__main__":
    main()
