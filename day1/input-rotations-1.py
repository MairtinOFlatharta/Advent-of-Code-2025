def main():
    out = read_rotations("rotations.txt")
    curr_position = 50
    num_zeroes = 0
    for num in out:
        new_position = (num + curr_position) % 100
        if new_position == 0:
            num_zeroes = num_zeroes + 1
        curr_position = new_position
    print(f"Times 0 was the current position on the dial: {num_zeroes}")

def read_rotations(file):
    with open(file, "r") as f:
        for line in f:
            direction = line[0]
            num = int(line[1:].strip())
            if direction == "L":
                # If dial is going left, convert rotation to a negative
                # number
                num *= -1
            yield (num)

if __name__ == "__main__":
    main()
