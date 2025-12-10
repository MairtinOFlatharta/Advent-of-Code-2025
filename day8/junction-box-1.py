import math

def main():
    coords = []
    distances = {}
    groups = []
    for line in read_input("input.txt"):
        coords.append(line)

    for i in range(0, len(coords)):
        for j in range(0, len(coords)):
            if i == j or distances.get((j, i), None) is not None:
                continue
            distances[(i, j)] = get_linear_distance(coords[i], coords[j])

    pairs_connected = 0
    while pairs_connected < 1000:
        group1, group2 = (-1, -1)
        shortest = min(distances, key=distances.get)

        for i in range(0, len(groups)):
            if shortest[0] in groups[i]:
                group1 = i
                break
        for i in range(0, len(groups)):
            if shortest[1] in groups[i]:
                group2 = i
                break

        if group1 == group2:
            if group1 == -1:
                # These junction boxes create a new circuit
                groups.append([*shortest])
            pairs_connected += 1
            del distances[shortest]
            continue

        if group1 != -1 and group2 == -1:
            groups[group1].append(shortest[1])
            pairs_connected += 1
        if group2 != -1 and group1 == -1:
            groups[group2].append(shortest[0])
            pairs_connected += 1
        if group1 != -1 and group2 != -1:
            # These 2 junction boxes already belong to 2 circuits,
            # so merge the circuits
            groups[group1].extend(groups[group2])
            del groups[group2]
            pairs_connected += 1

        del distances[shortest]
    group_sizes = [len(x) for x in groups]
    mult_sizes = 1
    for i in range(0, 3):
        mult_sizes *= max(group_sizes)
        group_sizes.remove(max(group_sizes))
    print(mult_sizes)


def get_linear_distance(c1, c2):
    distance = 0
    for i in range(0, len(c1)):
        distance += (c1[i] - c2[i]) ** 2
    return math.sqrt(distance)


def read_input(filename):
    with open(filename, "r") as f:
        for line in f:
            coords = line.strip().split(",")
            for i in range(0, len(coords)):
                coords[i] = int(coords[i])
            yield tuple(coords)


if __name__ == "__main__":
    main()
