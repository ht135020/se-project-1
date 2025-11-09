def insertion_sort(list):
    """In-place insertion sort."""
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = init


try:
    n = int(input("Enter the number of elements: "))
except ValueError:
    print("Please enter a valid integer for the number of elements.")
    raise SystemExit(1)

arr = []
for i in range(n):
    try:
        arr.append(int(input(f"Enter element {i+1}: ")))
    except ValueError:
        print("Please enter a valid integer.")
        raise SystemExit(1)

print("Array before:", arr)
insertion_sort(arr)
print("Array after:", arr)

    