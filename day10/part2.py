def to_from(fromd):
    return (fromd + 2) % 4

def next_coor(coor, dir):
    vector = directions[dir]
    new_coor = (coor[0] + vector[0], coor[1] + vector[1])
    pipe = maze[new_coor[0]][new_coor[1]]
    if pipe == 'S':
        return new_coor, 0

    for d in pipes[pipe]:
        if dir != to_from(d):
            to_dir = d
            break

    return new_coor, to_dir

input_path = 'day10/input/input.txt'

file = open(input_path).read().strip()
maze = file.split('\n')

#define directions N, E, S, W
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pipes = {'|': [0, 2], '-': [1, 3], 'L': [0, 1], 'J': [0, 3], '7': [2, 3], 'F': [1, 2]}


# find starting coordinate
start = ()
for i, line in enumerate(maze):
    if 'S' in line:
        start = (i, line.find('S'))
        break

# find adjacent open pipes
starting_to = 0
for i, d in enumerate(directions):
    pipe = maze[start[0] + d[0]][start[1] + d[1]]
    if to_from(i) in pipes[pipe]:
        starting_to = i
        break

path = []
coor = start
dir = starting_to

while coor != start or len(path) == 0:
    coor, dir = next_coor(coor, dir)
    path.append(coor)

# print(int((len(path)) / 2))
inside = False
count = 0
for i, row in enumerate(maze):
    for j, p in enumerate(row):
        if (i, j) in path:
            if p in 'L-J':
                continue
            inside = not inside
            continue
        if inside:
            count += 1
    inside = False

print(count)