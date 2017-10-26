def dominating_pairs(coords, current_index=0):
    if (current_index >= len(coords)):
        #BASE CASE: we cannot divide the space any further, time to add up our counts
        return 0
    else:
        count = 0
        coord = coords[current_index]

        for i in range(0, len(coords)):
            next_coord = coords[i]

            if (coord[0] > next_coord[0] and coord[1] > next_coord[1]):
                count += 1

        #RECURSIVE CASE: we've still got more to check
        return count + dominating_pairs(coords, current_index + 1)


def get_pairs(strng):
    arr = [int(i) for i in strng.split(' ')]
    pairs = []
    for i in range(0, len(arr), 2):
        coord_pair = [arr[i], arr[i+1]]
        pairs.append(coord_pair)

    return pairs


if __name__ == "__main__":
    i = input()

    coord_pairs = get_pairs(i)
    print(dominating_pairs(coord_pairs))