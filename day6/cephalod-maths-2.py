def main():
    data = []
    numbers = []
    operators = []
    for row in read_input("input.txt"):
        data.append(row)
    for i in range(0, len(data)-1):
        numbers.append(data[i])
    operators = data.pop()
    operators = parse_operators(operators)
    numbers = parse_numbers(numbers, operators)
    results = cephalod_maths(numbers, operators)
    print(f"Sum of results: {sum(results)}")


def parse_operators(raw):
    # Convert string of operators and spaces into list of tuples
    # where each tuple contains the operater and the max length
    # of numbers used in the operation, as all numbers have 1 space
    # between them
    # E.x. "+   * +   " => [("+", 3), ("*", 1), ("+", 4)]
    parsed = []
    for i in range(0, len(raw)):
        if raw[i] in "+*":
            operator = raw[i]
            index = i + 1
            space_count = 1
            while index < len(raw) and raw[index] in " \n":
                space_count += 1
                index += 1
            parsed.append((operator, space_count))
    return parsed


def parse_numbers(raw, operators):
    # Convert conventional numbers in input to the "right to left"
    # column numbers
    # E.x. [
    #     "123  54 3",
    #     "89  408 456",
    #     "5   110 909",
    # ] => [[3, 29, 185], [480, 501, 41], [69, 50, 349]]
    index = 0
    parsed_numbers = []
    for _, size in operators:
        numbers = []
        for i in range(index+size-2, index-1, -1):
            # Traverse current section from right to left
            number = ""
            for n in raw:
                number += n[i]
            numbers.append(int(number.replace(" ", "")))
        index += size
        parsed_numbers.append(numbers)
    return parsed_numbers


def cephalod_maths(numbers, operators):
    results = []
    for i in range(0, len(numbers)):
        # Build intial results list depending on the operator
        # (0 * anything = still 0)
        match operators[i][0]:
            case '+':
                results.append(0)
            case '*':
                results.append(1)

    for i in range(0, len(numbers)):
        for j in range(0, len(numbers[i])):
            match operators[i][0]:
                case '+':
                    results[i] += int(numbers[i][j])
                case '*':
                    results[i] *= int(numbers[i][j])
    return results


def read_input(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line


if __name__ == "__main__":
    main()
