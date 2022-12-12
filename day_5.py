from collections import defaultdict
import re


def append_value_to_map(key, value, stack_map):
    if type(value) is list:
        stack_map.setdefault(key, []).extend(value)
    else:
        stack_map.setdefault(key, []).append(value)
    return stack_map


def process_stack_line(line, stack_map):
    count = 1

    for i in range(0, len(line), 4):
        value = line[i:i + 3].strip().replace('[', '').replace(']', '')
        if value:
            stack_map = append_value_to_map(count, value, stack_map)
        count += 1

    return stack_map


def get_stacks_map(stacks):
    stacks.pop()
    stack_map = defaultdict(list)
    for line in stacks:
        stack_map = process_stack_line(line, stack_map)

    [v.reverse() for k, v in stack_map.items()]
    return stack_map


def regex_moves_to_map(line):
    match = re.search('move (.{1,2}) from (.) to (.)', line)
    return match.groups()


def get_moves_map(moves):
    moves_map = [list(map(int, regex_moves_to_map(line))) for line in moves]
    return moves_map


def make_single_move(single_move, stack_map, multiple):
    if multiple:
        n = single_move[0]
        containers = stack_map[single_move[1]][-n:]
        del stack_map[single_move[1]][-n:]
        stack_map = append_value_to_map(single_move[2], containers, stack_map)
        return stack_map

    for i in range(0, single_move[0]):
        container = stack_map[single_move[1]].pop()
        stack_map = append_value_to_map(single_move[2], container, stack_map)

    return stack_map


def rearrange_stacks(moves_map, stacks_map, multiple):
    for single_move in moves_map:
        stacks_map = make_single_move(single_move, stacks_map, multiple)

    return stacks_map


def get_top_stacks(stacks_file, moves_file, multiple):
    stacks_map = get_stacks_map([line for line in stacks_file])
    moves_map = get_moves_map([line for line in moves_file])
    stacks_map = rearrange_stacks(moves_map, stacks_map, multiple)
    return ''.join([v.pop() for k, v in sorted(stacks_map.items())])


with open("resources/stacks.txt", "r") as s, open('resources/moves.txt', 'r') as m:
    print(get_top_stacks(s, m, False))
    s.seek(0)
    m.seek(0)
    print(get_top_stacks(s, m, True))
