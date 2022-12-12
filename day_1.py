def count_calories(lines):
    totals = []
    total = 0
    for line in lines:
        if line.strip():
            total += int(line)
        else:
            totals.append(total)
            total = 0
    return totals


with open("resources/calorie_count.txt", "r") as f:
    totals = count_calories(f)

# First answer
print(max(totals))

totals.sort(reverse=True)
three_total = sum(totals[:3])
# Second answer
print(three_total)
