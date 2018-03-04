'''
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
'''
def zigzag_iterator(vectors):
    v_index = 0
    i = 0
    max_len = 0
    for v in vectors:
        max_len = max(max_len, len(v))
    while i <= max_len:
        if v_index < len(vectors) and i < len(vectors[v_index]):
            yield vectors[v_index][i]
        v_index += 1
        if v_index >= len(vectors):
            v_index = 0
            i += 1

vectors = [[1,2],[3,4,5,6]]
print vectors, ':',
for i in zigzag_iterator(vectors):
    print i,
print

vectors = [1,2,3], [4,5,6,7], [8,9]
print vectors, ':',
for i in zigzag_iterator(vectors):
    print i,
