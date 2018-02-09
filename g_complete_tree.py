def completeTreeLCA(num1, num2):
    while num1 > 1 or num2 > 1:
        if num1 == num2:
            return num1
        elif num1 > num2:
            num1 /= 2
        else:
            num2 /= 2
    return 1

assert completeTreeLCA(2, 10) == 2
assert completeTreeLCA(2, 8) == 2
assert completeTreeLCA(2, 12) == 1
assert completeTreeLCA(2, 11) == 2
assert completeTreeLCA(4, 5) == 2
assert completeTreeLCA(4, 6) == 1
