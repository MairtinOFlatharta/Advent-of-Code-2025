# NOTE: This solution IS NOT COMPLETE!!!!!
# It does not return the correct solution for input2.txt,
# so I just ended up getting lucky here :)

def main():
    points = []
    for entry in read_input("input.txt"):
        points.append(entry)

    areas = {}
    invalid_rect = {}
    lines = get_lines(points)
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            area = get_area(points[i], points[j], lines)
            if area is None:
                invalid_rect[(i, j)] = 1
                continue
            if i == j:
                continue
            if invalid_rect.get((points[j], points[i]), None) is not None:
                continue
            areas[(points[i], points[j])] = area
    max_points = max(areas, key=areas.get)
    print(f"Maximum possible area: {areas[max_points]}")


def read_input(filename):
    with open(filename, 'r') as f:
        for line in f:
            dat = line.strip().split(',')
            yield (int(dat[0]), int(dat[1]))


def get_area(p1, p2, lines):
    if not is_valid_rect(p1, p2, lines):
        return None
    l = abs(p1[0] - p2[0]) + 1
    h = abs(p1[1] - p2[1]) + 1
    return l * h


def get_lines(points):
    # Data: (point1, point2, outside direction (-1 or 1))
    lines = []
    lastHor = ()
    lastVer = ()
    for i in range(-1, len(points)-1):
        direction = 0
        isHor, isVer = (False, False)
        if points[i][0] == points[i+1][0]:
            isVer = True
        else:
            isHor = True

        lines.append((points[i], points[i+1], isVer))
    return lines


def is_valid_rect(c1, c2, lines):
    c3 = (c1[0], c2[1])
    c4 = (c2[0], c1[1])
    rect_lines = ((c1, c3), (c1, c4), (c2, c3), (c2, c4))
    for line in lines:
        # First, check if point falls in bounds of rectangle
        if line[0][0] > min(c1[0], c2[0]) and line[0][0] < max(c1[0], c2[0]):
            if line[0][1] > min(c1[1], c2[1]) and line[0][1] < max(c1[1], c2[1]):
                return False

        for rl in rect_lines:
            # Second, check if bounds of rectangle intersect with lines of
            # polygon
            isVert = False
            if rl[0][0] == rl[1][0]:
                isVert = True
            if isVert and line[2]:
                continue
            if not isVert and not line[2]:
                continue
            if isVert:
                if rl[0][0] > min(line[0][0], line[1][0]) and rl[0][0] < max(line[0][0], line[1][0]):
                    if min(rl[0][1], rl[1][1]) < line[0][1] and max(rl[0][1], rl[1][1]) > line[0][1]:
                        return False
            if not isVert:
                if rl[0][1] > min(line[0][1], line[1][1]) and rl[0][1] < max(line[0][1], line[1][1]):
                    if min(rl[0][0], rl[1][0]) < line[0][0] and max(rl[0][0], rl[1][0]) > line[0][0]:
                        return False
    return True


if __name__ == "__main__":
    main()
