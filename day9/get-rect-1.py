def main():
    points = []
    for entry in read_input("input.txt"):
        points.append(entry)

    areas = {}
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            area = get_area(points[i], points[j])
            if i == j:
                continue
            if areas.get((points[j], points[i]), None) is not None:
                continue
            areas[(points[i], points[j])] = area
    max_points = max(areas, key=areas.get)
    print(f"Maximum possible area: {areas[max_points]}")


def read_input(filename):
    with open(filename, 'r') as f:
        for line in f:
            dat = line.strip().split(',')
            yield (int(dat[0]), int(dat[1]))


def get_area(p1, p2):
    l = abs(p1[0] - p2[0]) + 1
    h = abs(p1[1] - p2[1]) + 1
    return l * h


if __name__ == "__main__":
    main()
