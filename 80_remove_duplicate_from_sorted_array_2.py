def removeDuplicates(nums):
    i, j = 0, 0
    previous_equal = False
    while j < len(nums):
        # print i,j, nums
        if j >=1 and nums[j] == nums[j-1]:
            if previous_equal:
                j += 1
                continue
            else:
                previous_equal = True
        else:
            previous_equal = False
        nums[i] = nums[j]
        i += 1
        j += 1
    return i

# n = [1,1,1,2,2,3]
n = [0,0,1,1,1,1,2,3,3]
print removeDuplicates(n)
print n
