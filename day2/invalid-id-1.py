def main():
    ranges = parse_input("input.txt")
    sum_invalid = 0
    for (lower, upper) in ranges:
        # Generate all possible numbers between range bounds
        curr_range = range(lower, upper)
        for num in curr_range:
            if is_pattern(num):
                sum_invalid += num
    print(f"Sum of invalid IDs: {sum_invalid}")

def is_pattern(num):
    curr = str(num)
    if len(curr) % 2 != 0:
        # Pattern must appear only twice, so an ID of an uneven length
        # cannot have a pattern
        return False
    half = int(len(curr)/2)
    if curr[0:half] == curr[half:]:
        # Check if both halves of the ID are equal
        return True
    return False

def parse_input(filename):
    content = ""
    with open(filename, "r") as f:
        for line in f:
            content = line.strip()
    ranges = content.split(",")
    for r in ranges:
        range_pair = r.split("-")
        yield (int(range_pair[0]), int(range_pair[1]))

if __name__ == "__main__":
    main()
