from sys import stdin


# start east
def main():
    y, x = 0, 0
    heading = 0
    headings = ["E", "S", "W", "N"]
    instructions = [line.strip() for line in stdin]
    wp_dx = 10
    wp_dy = 1
    for i in instructions:
        mov = i[0]
        num = int(i[1:])
        if mov == "R":
            for i in range(num // 90):
                wp_dx, wp_dy = rot_r(wp_dx, wp_dy)
        elif mov == "L":
            for i in range(num // 90):
                wp_dx, wp_dy = rot_l(wp_dx, wp_dy)
        elif mov == "N":
            wp_dy += num
        elif mov == "S":
            wp_dy -= num
        elif mov == "W":
            wp_dx -= num
        elif mov == "E":
            wp_dx += num
        elif mov == "F":
            x += num * wp_dx
            y += num * wp_dy
    print(abs(y) + abs(x))


def rot_r(xr, yr):
    return yr, -xr
            

def rot_l(xr, yr):
    return -yr, xr


if __name__ == "__main__":
    main()
