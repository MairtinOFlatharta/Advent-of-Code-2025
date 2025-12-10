from itertools import chain, combinations

def main():
    total_presses = 0
    for line in read_input("input.txt"):
        min_presses = 0
        presses = []
        goal = translate_goal(line[0])
        bin_buttons = []
        buttons = line[1:]
        for b in buttons:
            bin_buttons.append(translate_button(b, len(line[0])))
        for s in list(powerset(set(bin_buttons))):
            # Perform XOR on all buttons and see if it is
            # equal to goal
            res = 0
            for n in s:
                res ^= n
            if res == goal:
                presses.append(len(s))

        total_presses += min(presses)
    print(f"Total number of minimum presses: {total_presses}")


def translate_button(button, goal_length):
    # Store button as a binary string where
    # 1 = Affects cell, 0 = no effect
    # E.x. for goal len 6 (1, 4) => 10010
    bin_num = 0
    for space in button:
        bin_num += 1 << (goal_length - space - 1)
    return bin_num


def translate_goal(str_goal):
    # Store all indicies where the light must be on
    # E.x. '#..#.##' => [0, 3, 5, 6]
    # Convert string goal into binary string
    # Light on = 1, light off = 0
    goal = 0
    for c in range(0, len(str_goal)):
        if str_goal[c] == '#':
            goal += 1 << (len(str_goal) - c - 1)
    return goal


# This is an itertools recipe that I yoinked: https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def read_input(filename):
    with open(filename, 'r') as f:
        for line in f:
            raw = line.strip().split(" ")
            sanitized = []
            for i in range(0, len(raw)):
                if i == 0:
                    sanitized.append(raw[i].strip("[]"))
                    continue
                if i == len(raw)-1:
                    # Ignored for part 1
                    continue
                numbers = [int(x) for x in raw[i].strip("()").split(',')]
                sanitized.append(set(numbers))
            yield sanitized

if __name__ == "__main__":
    main()
