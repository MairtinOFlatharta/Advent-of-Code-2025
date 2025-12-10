def main():
    raw = []
    for line in read_input("input.txt"):
        raw.append(line)
    start = find_start(raw[0])
    paths = [0] * len(raw[0])

    for i in range(1, len(raw)-1):
        if i == 1:
            raw[i][start] = '|'
            paths[start] = 1
        for j in range(1, len(raw[0])-1):
            if is_beam(raw[i][j]):
                if is_split(raw[i+1][j]):
                    raw[i+1][j-1], raw[i+1][j+1] = ('|', '|')
                    paths[j-1] += paths[j]
                    paths[j+1] += paths[j]
                    paths[j] = 0
                if is_space(raw[i+1][j]):
                    raw[i+1][j] = '|'
    print(f"Number of paths: {sum(paths)}")


def find_start(line):
    for i in range(0, len(line)):
        if line[i] == 'S':
            return i
    return None


def is_split(char):
    if char == '^':
        return True
    return False


def is_beam(char):
    if char == '|':
        return True
    return False


def is_space(char):
    if char == '.':
        return True
    return False


def read_input(filename):
    with open(filename, "r") as f:
        for line in f:
            yield list(line.strip())


if __name__ == "__main__":
    main()
