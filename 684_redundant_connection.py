'''
We are given a "tree" in the form of a 2D-array, with distinct values for each node.

In the given 2D-array, each element pair [u, v] represents that v is a child of u in the tree.

We can remove exactly one redundant pair in this "tree" to make the result a tree.

You need to find and output such a pair. If there are multiple answers for this question, output the one appearing last in the 2D-array. There is always at least one answer.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: Original tree will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [1,3], [3,1]]
Output: [3,1]
Explanation: Original tree will be like this:
  1
 / \\
2   3
Note:
The size of the input 2D-array will be between 1 and 1000.
Every integer represented in the 2D-array will be between 1 and 2000.
'''
def findRedundantConnection(edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    hash_table = dict()
    edges_set = set()
    for e in edges:
        edges_set.add(tuple(e))
        if e[0] not in hash_table:
            hash_table[e[0]] = set()
        hash_table[e[0]].add(e[1])
        if e[1] not in hash_table:
            hash_table[e[1]] = set()
        hash_table[e[1]].add(e[0])
    print hash_table, edges_set

    for e in edges[::-1]:
        if tuple([e[1], e[0]]) in edges_set:
            return e
        hash_table[e[0]].remove(e[1])
        hash_table[e[1]].remove(e[0])
        cur_set = set()
        cur_set.add((e[0], 0))
        while True:
            print cur_set
            new_set = set()
            foundOne = False
            for elem in cur_set:
                if elem[1] == 0:
                    new_set.add((elem[0], 1))
                    for new_node in hash_table[elem[0]]:
                        if (new_node, 1) not in cur_set:
                            new_set.add((new_node, 0))
                    foundOne = True
                else:
                    new_set.add(elem)
            if not foundOne:
                break
            if (e[1], 0) in new_set:
                return e
            cur_set = new_set


# print findRedundantConnection([[1,2], [1,3], [2,3]])
# print findRedundantConnection([[1,2], [1,3], [3,1]])
# print findRedundantConnection([[1,2], [2,3], [3,1]])
print findRedundantConnection([[9,1],[2,10],[2,6],[8,7],[5,7],[8,9],[2,4],[3,7],[1,5],[4,7]])
