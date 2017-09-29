'''
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given a array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].
'''
def kEmptySlots(flowers, k):
    """
    :type flowers: List[int]
    :type k: int
    :rtype: int
    """
    # Convert array using day as index to array using flower as index.
    # NB: flower is zero-indexed, day is one-indexed.
    f_arr = [None for _ in xrange(len(flowers))]
    for i in xrange(len(flowers)):
        f = flowers[i]
        f_arr[f-1] = i + 1
    print f_arr

    l = 0
    r = k + 1
    cur = l
    result = 999999999
    while r < len(f_arr):
        print l, cur, r
        assert(cur <= r)
        assert(l <= cur)
        if cur == r:
            result = min(result, max(f_arr[l], f_arr[r]))
            l = cur
            r = l + k + 1
        elif f_arr[cur] < f_arr[l] or f_arr[cur] < f_arr[r]:
            l = cur
            r = l + k + 1
        cur += 1
    return result if result != 999999999 else -1

print kEmptySlots([2,4,1,8,5,6,7,3], 2)     # Expect day 5
print kEmptySlots([1,3,2], 1)     # Expect day 2
print kEmptySlots([1,2,3], 1)     # Expect -1
