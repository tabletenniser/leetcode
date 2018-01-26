'''
'''
def unique_substrings(string, k):
    result = set()
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
                result.add(''.join(cur_window))
            cur_unique_strs.remove(cur_window[0])
            del cur_window[0]
    print result
    return list(result)

assert set(unique_substrings("awaglknagawunagwkwag", 4)) == \
    set(["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun",
    "wuna", "unag", "nagw", "agwk", "kwag"])
assert set(unique_substrings("abcbcbcaaaaaadaaaaaa", 4)) == set()
