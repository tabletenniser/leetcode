'''
Given a list which can can contain elements as well as lists, write an
iterator to flatten a nested list
'''
def flatten_lst(lst):
    result = []
    for elem in lst:
        if type(elem) is list:
            result.extend(flatten_lst(elem))
        else:
            result.append(elem)
    return result

print flatten_lst([34,5,6,[4,5,6,[4,[5]],9],6])
