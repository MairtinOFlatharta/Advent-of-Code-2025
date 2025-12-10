def main():
    numbers = []
    operators = []
    for row in read_input("input.txt"):
        try:
            int(row[0])
            numbers.append(row)
        except:
            operators.extend(row)
    results = cephalod_maths(numbers, operators)
    print(f"Total sum of results: {sum(results)}")


def cephalod_maths(numbers, operators):
    results = []
    for i in range(0, len(operators)):
        # Build intial results list depending on the operator
        # (0 * anything = still 0)
        match operators[i]:
            case '+':
                results.append(0)
            case '*':
                results.append(1)

    for i in range(0, len(numbers)):
        for j in range(0, len(operators)):
            match operators[j]:
                case '+':
                    results[j] += int(numbers[i][j])
                case '*':
                    results[j] *= int(numbers[i][j])
    return results


def read_input(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.split()


if __name__ == "__main__":
    main()
