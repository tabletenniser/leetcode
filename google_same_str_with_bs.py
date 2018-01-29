# -*- coding: utf-8 -*-
'''
给两个char array，其中有一些char为backspace就是删除前面的字符，要求输出一个boolean判断两个char array是否相同，时间要求O(n) , 空间要求O(1)
例如：
[a,b,'\b',d,c] 和[a,d,c] true
[a,b,'\b','\b','\b',d,c] 和 [d,c] true
[a,b,d,'\b'] 和 [a,d] false

先给了用Stack的方法，TimeO(n), SpaceO(n)，没让写code
之后要求TimeO(n), SpaceO(1)，po主试着从前往后parse没成功，好久之后小哥给提示从后往前parse
试着写，po主渣，没写完
'''
def get_rid_of_backspaces(char_list, index):
    bs_count = 0
    while index < len(char_list) and (char_list[-index] == '\b' or bs_count > 0):
        if char_list[-index] == '\b':
            bs_count += 1
        elif bs_count > 0:
            bs_count -= 1
        index += 1
    return index

def same_str(str_a, str_b):
    print str_a, str_b
    i_a, i_b = 1, 1
    while True:
        i_a = get_rid_of_backspaces(str_a, i_a)
        i_b = get_rid_of_backspaces(str_b, i_b)
        if i_a == len(str_a) or i_b == len(str_b):
            return True

        if i_a >= len(str_a) or i_b >= len(str_b) or str_a[-i_a] != str_b[-i_b]:
            return False
        i_a += 1
        i_b += 1
    assert False

assert same_str(['a','b','\b','d','c'], ['a','d','c'])
assert same_str(['a','b','\b','\b','\b','d','c'], ['d','c'])
assert same_str(['a','b','d', '\b'], ['a','d']) == False
assert same_str(['a','b','d', '\b'], ['a','b'])
