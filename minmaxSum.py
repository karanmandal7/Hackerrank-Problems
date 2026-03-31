def minmaxSum(arr):
    total = sum(arr)
    minimum = total - max(arr)
    maximum = total - min(arr)

    print(minimum, maximum)

numbers = [2, 4, 5, 6, 7]

minmaxSum(numbers)