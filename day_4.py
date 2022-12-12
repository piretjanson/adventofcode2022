def has_same_sections(first_set, second_set):
    return len(first_set & second_set) > 0


def is_fully_overlapping(first_set, second_set):
    return first_set.issubset(second_set) or second_set.issubset(first_set)


def get_sections_overlap(line, fully):
    sections = line.split(',')
    first_section = [int(x) for x in sections[0].split('-')]
    second_section = [int(x) for x in sections[1].split('-')]
    if fully:
        return int(is_fully_overlapping(set((range(first_section[0], (first_section[1]) + 1))),
                                        set((range(second_section[0], (second_section[1]) + 1)))))

    return int(has_same_sections(set((range(first_section[0], (first_section[1]) + 1))),
                                 set((range(second_section[0], (second_section[1]) + 1)))))


def count_range_overlaps(file, fully):
    lines = [line.rstrip() for line in file]
    return sum([get_sections_overlap(line, fully) for line in lines])


with open("resources/assignments.txt", "r") as f:
    print(count_range_overlaps(f, True))
    f.seek(0)
    print(count_range_overlaps(f, False))
