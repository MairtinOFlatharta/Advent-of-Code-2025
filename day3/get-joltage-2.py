def main():
    lines = get_input("input.txt")
    sum_joltage = 0
    for l in lines:
        sum_joltage += get_highest_joltage(l)
    print(f"Sum of highest joltage: {sum_joltage}")

def get_highest_joltage(bank):
    bank_len = len(bank)
    digits = []
    last_pos = -1
    curr_dig = ""
    for i in range(0, 12):
        # Start searching after the last found digit, while leaving
        # space for the digits that come after
        curr_dig, last_pos = get_highest_digit(bank, last_pos+1, bank_len-(12-i))
        digits.append(curr_dig)
    return int(list_to_str(digits))

def list_to_str(l):
    res = ""
    for string in l:
        # Concatenate all the strings in order
        res += string
    return res

def get_highest_digit(data, lower, upper):
    i = lower
    highest = ""
    pos = 0
    while i <= upper:
        if data[i] > highest:
            # Keep track of the highest digit and its index position
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
