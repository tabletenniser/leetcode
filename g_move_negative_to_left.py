'''
1. given an integer array, move all negative numbers to the left
[-1,3,0,-2,5] - > [-1,-2,0,3,5]
'''
def move_negative_to_left(lst):
    print lst
    i, j = 0, 0
    while j < len(lst):
        if lst[j] < 0:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1
    print lst
    return

lst = [-1,3,0,-2,5]
move_negative_to_left(lst)
assert lst == [-1,-2,0,3,5]

lst = [-1,-3,-4,-2,-8]
move_negative_to_left(lst)
assert lst == [-1, -3, -4, -2, -8]

lst = [1,3,4,2,8]
move_negative_to_left(lst)
assert lst == [1, 3, 4, 2, 8]
