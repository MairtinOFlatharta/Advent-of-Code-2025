def main():
    lines = get_input("input.txt")
    sum_joltage = 0
    for l in lines:
        sum_joltage += get_highest_joltage(l)
    print(f"Sum of highest joltage: {sum_joltage}")

def get_highest_joltage(bank):
    bank_len = len(bank)
    # For the first digit, look at all digits except for the last one
    dig1, pos = get_highest_digit(bank, 0, bank_len-2)
    # For the second digit, start after the position of the first digit
    # and continue to the end of the string
    dig2, _ = get_highest_digit(bank, pos+1, bank_len-1)
    return int(dig1 + dig2)

def get_highest_digit(data, lower, upper):
    i = lower
    highest = ""
    pos = 0
    while i <= upper:
        if data[i] > highest:
            # Keep track of highest digit and its index position
            highest = data[i]
            pos = i
        i += 1
    return (highest, pos)

def get_input(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

if __name__ == "__main__":
    main()
