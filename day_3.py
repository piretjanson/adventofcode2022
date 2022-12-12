import string


def find_type_priority(duplicate):
    return string.ascii_letters.index(duplicate) + 1


def get_line_priority(line):
    line = line.strip()
    duplicate_type = set(line[:len(line) // 2]) & set(line[len(line) // 2:])
    return find_type_priority(duplicate_type.pop())


def get_group_priority(group_lines):
    badge = set(group_lines[0]) & set(group_lines[1]) & set(group_lines[2])
    return find_type_priority(badge.pop())


def calculate_total_priorities(file, group):
    lines = [line.rstrip() for line in file]

    if group:
        total = 0
        for i in range(0, len(lines), 3):
            total += get_group_priority(lines[i:i + 3])
        return total

    return sum([get_line_priority(line) for line in lines])


with open("resources/rucksacks_content.txt", "r") as f:
    print(calculate_total_priorities(f, False))
    f.seek(0)
    print(calculate_total_priorities(f, True))
