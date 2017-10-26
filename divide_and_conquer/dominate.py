from functools import cmp_to_key


def coord_comparison(p1, p2):
    y_diff = p1[1] - p2[1]
    if y_diff != 0:
        return y_diff
    return p1[0] - p2[0]


def comparator(threshold):
    return coord_comparison(p1, p2)


def dominating_pairs(ordered_coordinates):
    if len(ordered_coordinates) == 2 or len(ordered_coordinates) == 1:
        return 0 if len(ordered_coordinates) == 1 or ordered_coordinates[0][1] > ordered_coordinates[1][1] else 1

    half_len = len(ordered_coordinates)//2
    left = sorted(ordered_coordinates[:half_len], key=lambda k: k[1])
    right = sorted(ordered_coordinates[half_len:], key=lambda k: k[1])

    i, j, count = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            count += len(right) - j
            i += 1
        else:
            j += 1

    return count + dominating_pairs(ordered_coordinates[:half_len]) + dominating_pairs(ordered_coordinates[half_len:])


def get_pairs(strng):
    arr = [int(i) for i in strng.strip().split(' ')]
    pairs = []
    for i in range(0, len(arr), 2):
        coord_pair = [arr[i], arr[i+1]]
        pairs.append(coord_pair)

    return pairs

if __name__ == "__main__":
    points = [int(i) for i in input().strip().split()]
    coordinates = sorted([(points[i], points[i+1]) for i in range(0, len(points), 2)], key=lambda k: k[0])
    print(dominating_pairs(coordinates))
