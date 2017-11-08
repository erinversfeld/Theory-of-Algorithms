def find_max_contiguous_subarray(arr):
    subarray = []
    subarray.append(0)

    for i in range(1, len(arr) + 1):
        subarray.append(max(subarray[i-1] * arr[i-1], arr[i-1]))

    max_product = max(subarray)
    final_index = subarray.index(max_product) - 1
    start_index = final_index

    for i in range(final_index, -1, -1):
        max_product = max_product/arr[i]
        if max_product == 1:
            start_index = i
            break

    return (final_index - start_index) + 1


if __name__ == "__main__":
    input_string = input()
    # input_string = '0.1 20 5 6.6 7 0 20 0.01 0.5 0.0067'
    arr = []
    for num in input_string.split(' '):
        try:
            arr.append(int(num))
        except ValueError:
            try:
                arr.append(float(num))
            except ValueError as v:
                print('Unexpected input character: ' + str(num))
                raise v
    max_contiguous_subarray = find_max_contiguous_subarray(arr)
    print(max_contiguous_subarray)