def main():
    ingredients = get_ingredients("input.txt")
    for r in get_fresh_ranges("input.txt"):
        for ing_id in ingredients.keys():
            if ing_id >= r[0] and ing_id <= r[1]:
                ingredients[ing_id] = True
    num_fresh = sum(1 for v in ingredients.values() if v == True)
    print(f"Number of fresh ingredients: {num_fresh}")


def get_ingredients(filename):
    # Get to ingredient IDs in file and create dictionary where
    # Key = ID and Value = Bool (False = spoiled, True = Fresh)
    newline_reached = False
    ingredients = {}
    with open(filename, "r") as f:
        for line in f:
            if newline_reached:
                # Initialize each value as spoiled
                ingredients[int(line.strip())] = False
            if line == "\n":
                newline_reached = True
    return ingredients


def get_fresh_ranges(filename):
    with open(filename, "r") as f:
        for line in f:
            if line == "\n":
                return
            upper, lower = line.strip().split("-")
            yield (int(upper), int(lower))

if __name__ == "__main__":
    main()
