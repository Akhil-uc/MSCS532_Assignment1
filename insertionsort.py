def insertion_sort_descending_b(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    insertion_sort_descending_b(arr, n - 1)
    last_element = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] < last_element:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last_element
    return arr
