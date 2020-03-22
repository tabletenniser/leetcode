'''

Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.

'''

class CustomStack:

    def __init__(self, maxSize: int):
        self._max_size = maxSize
        self._stack = [None for _ in range(maxSize)]
        self._cur_index = 0
        self._cur_size = 0

    def push(self, x: int) -> None:
        if self._cur_size >= self._max_size:
            return
        self._stack[self._cur_index % self._max_size] = x
        self._cur_index += 1
        self._cur_size += 1

    def pop(self) -> int:
        if self._cur_size <= 0:
            return -1
        num = self._stack[self._cur_index % self._max_size - 1]
        self._cur_index -= 1
        self._cur_size -= 1
        return num

    def increment(self, k: int, val: int) -> None:
        k = min(k, self._max_size)
        start_index = self._cur_index - self._cur_size
        for i in range(start_index, start_index + k):
            self._stack[i % self._max_size] += val

# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
print(obj._stack, obj._cur_size, obj._cur_index)
param_2 = obj.pop()
assert(param_2==2)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj._stack, obj._cur_size, obj._cur_index)
obj.increment(5,100)
print(obj._stack, obj._cur_size, obj._cur_index)
obj.increment(2,100)
assert(obj.pop() == 103)
assert(obj.pop() == 202)
assert(obj.pop() == 201)
assert(obj.pop() == -1)
