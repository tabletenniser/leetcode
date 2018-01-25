'''
'''
def unique_substrings(string, k):
    result = []
    cur_unique_strs = set()
    cur_window = []

    for ch in string:
        if ch in cur_unique_strs:
            while cur_window[0] != ch:
                cur_unique_strs.remove(cur_window[0])
                del cur_window[0]
            del cur_window[0]

        cur_unique_strs.add(ch)
        cur_window.append(ch)
        if len(cur_window) == k:
            if len(cur_unique_strs) == k:
                result.append(''.join(cur_window))
            cur_unique_strs.remove(cur_window[0])
            del cur_window[0]
    print result
    return result

assert unique_substrings("awaglknagawunagwkwag", 4) == \
    ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun",
    "wuna", "unag", "nagw", "agwk", "kwag"]
