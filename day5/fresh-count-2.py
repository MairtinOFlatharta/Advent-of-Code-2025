def main():
    ranges = []
    for r in get_fresh_ranges("input.txt"):
        ranges.append(r)

    # Sort ranges by the lower bound value
    ranges.sort(key=lambda tup: tup[0])

    # This will keep track of which index in grouped_ranges
    # that has the highest upper bound value
    top_index = 0
    grouped_ranges = []

    for r in ranges:
        if len(grouped_ranges) == 0:
            grouped_ranges.append(r)
            continue
        if is_overlapping(grouped_ranges[top_index], r):
            if r[1] > grouped_ranges[top_index][1]:
                # Both ranges are overlapping, so extend the existing range
                # to include the higher upper bound
                grouped_ranges[top_index] = (grouped_ranges[top_index][0], r[1])
            continue

        # Current range does not overlap, so add to the list
        # and use it as the new highest range
        grouped_ranges.append(r)
        top_index += 1

    num_fresh_ids = 0
    for r in grouped_ranges:
        num_ids = (r[1] - r[0]) + 1
        num_fresh_ids += num_ids

    print(f"Number of possible fresh IDs: {num_fresh_ids}")


def is_overlapping(r1, r2):
    # Arguments will be sorted by the lower bound of the range,
    # so this is simplified
    if r1[1] >= r2[0]:
        return True
    return False


def get_fresh_ranges(filename):
    with open(filename, "r") as f:
        for line in f:
            if line == "\n":
                return
            upper, lower = line.strip().split("-")
            yield (int(upper), int(lower))

if __name__ == "__main__":
    main()
