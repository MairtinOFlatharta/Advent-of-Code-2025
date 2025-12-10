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
    factors = get_factors(len(curr))

    for f in factors:
        parts = []
        i = 0
        while i < len(curr):
            # Split ID into equal parts
            parts.append(curr[i:i+f])
            i += f
        if len(set(parts)) == 1:
            # If all parts of the ID are the same,
            # a pattern has been found
            return True
    return False


def get_factors(num):
    # Find all factors except for the number itself
    i = 1
    factors = []
    while i <= num / 2:
        if num % i == 0:
            factors.append(i)
        i += 1
    return factors

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
