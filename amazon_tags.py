def subtags(targetList, availableTagList):
    target_set = set()
    for target_string in targetList:
        target_set.add(target_string.lower())
    cur_set = dict()
    left, right = 0, 0
    result = [0]
    min_window_size = 9999999

    while right < len(availableTagList):
        tag = availableTagList[right].lower()
        if tag in target_set:
            cur_set[tag] = cur_set.get(tag, 0) + 1
        right += 1
        while len(cur_set) == len(target_set):
            if right - left < min_window_size:
                min_window_size = right - left
                result = [left, right - 1]
            tag = availableTagList[left].lower()
            if tag in target_set:
                cur_set[tag] -= 1
                if cur_set[tag] == 0:
                    del cur_set[tag]
            left += 1
    print result, target_set
    return result

assert subtags(["2abc", "bcd", "cab"], ["dbc", "2abc", "cab", "bcd", "bcb"]) == [1,3]
assert subtags(["m", "i", "s"], ["m", "i", "h", "s", "i", "h", "m", "s", "s", "y"]) == [0, 3]
assert subtags(["m", "i", "S", "4"], ["m", "w", "f", "h", "t", "m", "r", "i", "s", "y"]) == [0]
