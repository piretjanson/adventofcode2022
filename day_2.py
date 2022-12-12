score_mapping = {
    "A": 1,
    "B": 2,
    "C": 3
}

defeat_map = {
    "A": "C",
    "C": "B",
    "B": "A"
}

letter_map = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

result_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def get_letter(first, result):
    if result == "X":
        return defeat_map[first]

    if result == "Y":
        return first

    return list(defeat_map.keys())[list(defeat_map.values()).index(first)]


def get_result_score(first, second):
    if first == second:
        return 3

    if defeat_map[second] == first:
        return 6

    return 0


def get_round_score(first_letter, second_letter, part):
    if part == 1:
        return score_mapping[letter_map[second_letter]] + get_result_score(first_letter, letter_map[second_letter])
    if part == 2:
        choice = get_letter(first_letter, second_letter)
        return score_mapping[choice] + result_score[second_letter]


def calculate_total_score(file, part):
    total = 0
    for line in file:
        if line.strip():
            total += get_round_score(line[0], line[2], part)
    return total


with open("resources/strategy_guide.txt", "r") as f:
    print(calculate_total_score(f, 1))
    f.seek(0)
    print(calculate_total_score(f, 2))
