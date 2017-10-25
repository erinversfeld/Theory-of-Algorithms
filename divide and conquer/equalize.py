from functools import reduce


def common_multiple_with_two(int_list):
    pass


def lowest_common_multiple(a, b):
    greater = a
    if a < b:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break

        greater += 1

    return lcm


def calc_lowest_common_multiple(int_list):
    return reduce(lambda x, y: lowest_common_multiple(x, y), int_list)


if __name__ == "__main__":
    print(calc_lowest_common_multiple([628, 1256, 628, 2512, 1256]))
