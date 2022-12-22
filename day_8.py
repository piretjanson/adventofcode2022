import math

matrix = []


def left_blocking_tree(x, y, tree_height):
    global matrix
    for i in range(x - 1, -1, -1):
        if matrix[y][i] >= tree_height:
            return i
    return -1


def top_blocking_tree(x, y, tree_height):
    global matrix
    for i in range(y - 1, -1, -1):
        if matrix[i][x] >= tree_height:
            return i
    return -1


def right_blocking_tree(x, y, tree_height):
    global matrix
    for i in range(x + 1, len(matrix[0])):
        if matrix[y][i] >= tree_height:
            return i
    return -1


def bottom_blocking_tree(x, y, tree_height):
    global matrix
    for i in range(y + 1, len(matrix)):
        if matrix[i][x] >= tree_height:
            return i
    return -1


def is_tree_visible(x, y, tree_height):
    visible_from_left = left_blocking_tree(x, y, tree_height)
    visible_from_top = top_blocking_tree(x, y, tree_height)
    visible_from_right = right_blocking_tree(x, y, tree_height)
    visible_from_bottom = bottom_blocking_tree(x, y, tree_height)
    return visible_from_left == -1 or visible_from_top == -1 or visible_from_right == -1 or visible_from_bottom == -1


def calculate_tree_visibility_score(x, y, tree_height):
    global matrix
    scores = []
    left_tree = left_blocking_tree(x, y, tree_height)
    top_tree = top_blocking_tree(x, y, tree_height)
    right_tree = right_blocking_tree(x, y, tree_height)
    bottom_tree = bottom_blocking_tree(x, y, tree_height)

    scores.append(x - left_tree if left_tree != -1 else x)
    scores.append(y - top_tree if top_tree != -1 else y)
    width = len(matrix[0]) - 1
    scores.append(right_tree - x if right_tree != -1 else width - x)
    length = len(matrix) - 1
    scores.append(bottom_tree - y if bottom_tree != -1 else length - y)

    return math.prod(scores)


def count_visible_trees():
    global matrix
    count_visible = (len(matrix[0]) * 2) + (len(matrix) * 2) - 4

    for y in range(1, (len(matrix) - 1)):
        for x in range(1, (len(matrix[0]) - 1)):
            tree_height = matrix[y][x]
            if is_tree_visible(x, y, tree_height):
                count_visible += 1

    return count_visible


def find_largest_score():
    global matrix
    scores = []
    for y in range(1, (len(matrix) - 1)):
        for x in range(1, (len(matrix[0]) - 1)):
            tree_height = matrix[y][x]
            scores.append(calculate_tree_visibility_score(x, y, tree_height))

    return max(scores)


def process_command_lines(lines, part1):
    global matrix
    matrix = [list(map(int, list(line.strip()))) for line in lines]
    if part1:
        return count_visible_trees()

    return find_largest_score()


with open("resources/grid_tree_map.txt", "r") as f:
    print('Part 1:')
    print(process_command_lines(f.readlines(), True))
    f.seek(0)
    print('Part 2:')
    print(process_command_lines(f.readlines(), False))
