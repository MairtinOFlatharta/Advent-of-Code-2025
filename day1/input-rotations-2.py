def main():
    out = read_rotations("rotations.txt")
    curr_position = 50
    num_zeroes = 0
    for num in out:
        new_position = num + curr_position
        if new_position == 0: 
            num_zeroes += 1
        if new_position < 0 and curr_position != 0:
            # Don't add to the number of zero passes if the dial
            # started at zero
            num_zeroes += 1

        # Calculate number of full dial rotations done
        num_zeroes += abs(int(new_position/100))

        # Normalize position
        curr_position = new_position % 100
    print(f"Times 0 was passed on the dial: {num_zeroes}")

def read_rotations(file):
    with open(file, "r") as f:
        for line in f:
            direction = line[0]
            num = int(line[1:].strip())
            if direction == "L":
                # If dial is rotated left, convert the rotation
                # to a negative number
                num *= -1
            yield (num)

if __name__ == "__main__":
    main()
