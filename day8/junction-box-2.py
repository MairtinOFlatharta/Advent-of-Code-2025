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

    last_pair = (-1, -1)
    while True:
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
            del distances[shortest]
            continue

        if group1 != -1 and group2 == -1:
            groups[group1].append(shortest[1])
        if group2 != -1 and group1 == -1:
            groups[group2].append(shortest[0])
        if group1 != -1 and group2 != -1:
            # These 2 junction boxes already belong to 2 circuits,
            # so merge the circuits
            groups[group1].extend(groups[group2])
            del groups[group2]

        del distances[shortest]
        if len(groups[0]) == 1000:
            last_pair = shortest
            break
    ans = coords[last_pair[0]][0] * coords[last_pair[1]][0]
    print(ans)


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
