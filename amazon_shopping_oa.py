import heapq as hq
def bestCombos(popularity, k):
    min_heap = [0]
    for p in popularity:
        new_elems = []
        for elem in min_heap:
            new_elems.append(elem+p)
        for new_elem in new_elems:
            hq.heappush(min_heap, new_elem)
        while len(min_heap) > 2000:
            hq.heappop(min_heap)
    min_heap.sort(reverse=True)
    # print(min_heap)
    return min_heap[:k]

popularity=[3,5,-2]
k = 3
assert bestCombos(popularity, k) == [8,6,5]
