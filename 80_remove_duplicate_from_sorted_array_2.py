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

def removeDuplicates2(nums):
    i, j, c, r = 0, 0, 0, 0
    while j < len(nums):
        # print i,j,c,r,nums
        if nums[i] == nums[j]:
            c += 1
            j += 1
            continue
        assert c > 0
        if c == 1:
            i = j
            r += 1
        else:
            i += 2
            nums[i:] = nums[j:]
            j = i
            r += 2
        c = 0
    r += min(c, 2)
    return r

n = [1,1,1]
# n = [0,0,1,1,1,1,2,3,3]
print removeDuplicates2(n)
print n
