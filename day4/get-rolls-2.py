def main():
    total_rolls_removed = 0
    rolls_removed = 1
    layout = read_input("input.txt")
    num_rows = len(layout)
    while rolls_removed > 0:
        rolls_removed = 0
        # This list will hold the next state of the warehouse
        layout_copy = []
        for i in range(0, num_rows):
            layout_copy.append("")
            for j in range(0, len(layout[i])):
                res = False
                if not is_paper(layout[i][j]):
                    layout_copy[i] += "."
                    continue
                if i == 0:
                    # Currently looking at top row
                    res = is_accessible(j, layout[i], None, layout[i+1])
                elif i == num_rows - 1:
                    # Currently looking at bottom row
                    res = is_accessible(j, layout[i], layout[i-1], None)
                else:
                    res = is_accessible(j, layout[i], layout[i-1], layout[i+1])

                if res:
                    # Cell is accessible, remove paper
                    layout_copy[i] += "."
                    rolls_removed += 1
                else:
                    layout_copy[i] += "@"
        total_rolls_removed += rolls_removed
        # Move to next state
        layout = layout_copy.copy()

    print(f"Number of rolls removed: {total_rolls_removed}")


def is_accessible(index, curr_row, upper, lower):
    num_neighbours = 0
    max_neighbours = 3
    if upper is not None:
        num_neighbours += get_num_paper(index, upper)

    if lower is not None:
        num_neighbours += get_num_paper(index, lower)

    num_neighbours += get_num_paper(index, curr_row) - 1

    if num_neighbours <= max_neighbours:
        return True
    return False


def get_num_paper(index, row):
    num_paper = 0
    row_len = len(row)

    # Check if current, previous, and next indexes are paper
    # Also account for edge cases
    if index > 0:
       if is_paper(row[index-1]):
            num_paper += 1
    if index < row_len-1:
        if is_paper(row[index+1]):
            num_paper += 1
    if is_paper(row[index]):
        num_paper += 1

    return num_paper


def is_paper(slot):
    if slot == "@":
        return True
    return False


def read_input(filename):
    content = []
    with open(filename, "r") as f:
        for line in f:
            content.append(line.strip())
    return content


if __name__ == "__main__":
    main()
