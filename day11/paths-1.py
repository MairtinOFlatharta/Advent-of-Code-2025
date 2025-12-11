def main():
    data = read_input("input.txt")
    print(data)


def read_input(filename):
    data = {}
    with open(filename, 'r') as f:
        for line in f:
            raw = line.strip().replace(':', '').split()
            outputs = raw[1:]
            data[raw[0]] = outputs
    return data


if __name__ == "__main__":
    main()
