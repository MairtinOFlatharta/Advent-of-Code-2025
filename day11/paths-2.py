num_paths = 0
data = {}

def main():
    global data
    data = read_input("input.txt")
    # Memoization dictionaries to speed up the process
    memo1 = {}
    memo2 = {}
    memo3 = {}
    # Since the graph is not cyclic, find paths
    # between each relevant node
    # A valid path will be either:
    # svr -> dac -> fft -> out OR
    # svr -> fft -> dac -> out
    dac_out = traverse("dac", "out", memo1)
    fft_dac = traverse("fft", "dac", memo2)
    svr_fft = traverse("svr", "fft", memo3)
    fft_out = traverse("fft", "out", memo1)
    dac_fft = traverse("dac", "fft", memo3)
    svr_dac = traverse("svr", "dac", memo2)
    print((svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out))


def traverse(device, end, memo):
    global data
    if device == end:
        return 1
    elif device == "out":
        return 0
    if device in memo:
        return memo[device]
    memo[device] = sum(traverse(d, end, memo) for d in data[device])
    return memo[device]


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
