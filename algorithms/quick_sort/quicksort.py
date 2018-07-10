import random


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[random.randrange(0, len(arr))]
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def main():
    print(quicksort([11, 900, 888, 23, 54, 2192, 3, 89, 75, 64, 45]))


if __name__ == "__main__":
    main()
