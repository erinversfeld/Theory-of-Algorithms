def equalised(nums):
    nums = list(set(nums)) #dedup
    nums.sort()

    max = nums[-1]

    # some sneaky lightweight optimisations like deduping
    if max != 0:
        try:
            nums.remove(0)
            return -1
        except Exception:
            pass
    elif len(nums) != 1:
        return -1 #deduping means that if the highest number is 0 and there are more numbers in the list, they will never multiply to 0 as 2^n can never be 0
    else:
        return 0

    for num in nums[:-1]:
        if num < max:
            # is it possible to multiply our way to this number with 2s only?
            rem = max//num
            if rem%2 != 0:
                return -1

    return max


if __name__ == "__main__":
    i = input()
    nums = [int(i) for i in i.strip().split(' ')]
    print(equalised(nums))
