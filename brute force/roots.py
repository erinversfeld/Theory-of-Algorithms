def modular_roots(n, x):
    square_roots = []
    mod = x % n
    for i in range(1, n):
        sq = pow(i, 2)
        if sq == mod:
            square_roots.append(str(i))
        elif sq > n:
            if sq % n == mod:
                square_roots.append(str(i))

    return square_roots


if __name__ == "__main__":
    num_n = int(input())
    num_x = int(input())

    print(' '.join(modular_roots(num_n, num_x)))
