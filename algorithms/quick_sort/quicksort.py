def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def main():
    print(quicksort([11, 900, 888, 23, 54, 2192, 3, 89, 75, 64, 45]))


if __name__ == "__main__":
    main()
