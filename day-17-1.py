from collections import deque
from copy import deepcopy
from sys import stdin

def main():
    layers = {0: get_first_layer()}
    for _ in range(6):
        layers = cycle(layers)
    l1 = [v for v in layers.values()]
    print(sum([l.count("#") for v in layers.values() for l in v]))


def get_first_layer():
    return deque([deque(line.strip()) for line in stdin])


def cycle(layers):
    pad(layers)
    return create_new_layers(layers)


def pad(layers):
    pad_rows(layers)
    pad_columns(layers)
    pad_layers(layers)


def pad_rows(layers):
    row_len = len(layers[0])
    empty_row = deque("." * row_len)
    for l in layers.values():
        l.appendleft(deepcopy(empty_row))
        l.append(deepcopy(empty_row))


def pad_columns(layers):
    for l in layers.values():
        for row in l:
            row.appendleft(".")
            row.append(".")


def pad_layers(layers):
    rows = len(layers[0])
    cols = len(layers[0][1])
    empty_layer = deque([deque("." * cols) for _ in range(rows)])
    layers[min(layers.keys()) - 1] = deepcopy(empty_layer)
    layers[max(layers.keys()) + 1] = deepcopy(empty_layer)


def create_new_layers(layers):
    new_layers = deepcopy(layers)
    # WHY didn't it even OCCUR to me to generate these?
    dirs = [
        [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [1, 1, 0], [1, -1, 0], [-1, 1, 0], [-1, -1, 0],
        [0, 1, 1], [0, -1, 1], [1, 0, 1], [-1, 0, 1], [1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1],
        [0, 1, -1], [0, -1, -1], [1, 0, -1], [-1, 0, -1], [1, 1, -1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1],
        [0, 0, 1], [0, 0, -1]
    ]
    rows = len(layers[0])
    cols = len(layers[0][0])
    for z in layers:
        for y in range(rows):
            for x in range(cols):
                neighbors = []
                for d in dirs:
                    z1 = z + d[2]
                    y1 = y + d[1]
                    x1 = x + d[0]
                    if z1 in layers and 0 <= y1 < rows and 0 <= x1 < cols:
                        neighbors.append(layers[z1][y1][x1])
                if layers[z][y][x] == ".":
                    new_layers[z][y][x] = "#" if neighbors.count("#") == 3 else "."
                else:
                    new_layers[z][y][x] = "#" if neighbors.count("#") in [2, 3] else "."
    return new_layers


if __name__ == "__main__":
    main()


'''
create a 'shell' around the existing space
- prepend/append an empty row to each layer. make empty rows the same length as existing rows
- prepend/append an empty item to each row including the empty rows just added
- create empty layers with indices one less than the existing min and one more than the existing max
copy existing space to new space
for each item in existing space get neighbors
- look in each direction
- add item to list if it exists
- else just ignore that direction
based on rules/neighbors set value of corresponding item in new space
'''
