from sys import stdin


# start east
def main():
    dy, dx = 0, 0
    heading = 0
    headings = ["E", "S", "W", "N"]
    instructions = [line.strip() for line in stdin]
    for i in instructions:
        mov = i[0]
        num = int(i[1:])
        if mov == "R":
            heading += num // 90
        elif mov == "L":
            heading -= num // 90
        elif mov == "N":
            dy += num
        elif mov == "S":
            dy -= num
        elif mov == "W":
            dx -= num
        elif mov == "E":
            dx += num
        elif mov == "F":
            dir_ = headings[heading % 4]
            if dir_ == "N":
                dy += num
            elif dir_ == "S":
                dy -= num
            elif dir_ == "W":
                dx -= num
            elif dir_ == "E":
                dx += num
    print(abs(dy) + abs(dx))
            


if __name__ == "__main__":
    main()
