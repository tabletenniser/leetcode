def quicksort(lst, low, high):
    if high - low <= 1:
        return
    pivot = lst[high-1]
    i, j = low, low
    while j < high - 1:
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1
    lst[i], lst[high-1] = lst[high-1], lst[i]
    quicksort(lst, low, i)
    quicksort(lst, i+1, high)
    return lst

print quicksort([1,2,3], 0, 3)
print quicksort([3,1,4], 0, 3)
print quicksort([3,1], 0, 2)

lst = [34,1,5,1,5,7,1,6,4,6,71,4]
quicksort(lst, 0, len(lst))
print lst, sorted(lst)
assert lst == sorted(lst)
