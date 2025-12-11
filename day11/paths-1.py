num_paths = 0

def main():
    data = read_input("input.txt")
    traverse("you", data)
    print(f"Total number of paths: {num_paths}")


def traverse(device, devices):
    global num_paths
    for d in devices[device]:
        if d == "out":
            num_paths += 1
            return
        traverse(d, devices)


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
