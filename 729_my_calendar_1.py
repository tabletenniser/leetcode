'''
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
'''
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.__dict__)

class MyCalendar_2(object):
    def __init__(self):
        self.root = None

    def overlap(self, node1, node2):
        if node1.end <= node2.start or node2.end <= node1.start:
            return False
        return True

    def insert(self, node, new_node):
        if self.overlap(node, new_node):
            return False
        if new_node.end <= node.start and \
                (node.left == None or new_node.start >= node.left.end):
            old_left = node.left
            node.left = new_node
            new_node.left = old_left
            return True
        if node.left != None and new_node.start < node.start:
            return self.insert(node.left, new_node)

        if new_node.start >= node.end and \
                (node.right == None or new_node.end <= node.right.start):
            old_right = node.right
            node.right = new_node
            new_node.right = old_right
            return True
        if node.right != None and new_node.start > node.start:
            return self.insert(node.right, new_node)
        assert False

    def print_tree(self, node):
        if node == None:
            return
        self.print_tree(node.left)
        print node.start, node.end
        self.print_tree(node.right)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # print "print_tree"
        # self.print_tree(self.root)

        new_node = Node(start, end)
        if self.root == None:
            self.root = new_node
            return True
        return self.insert(self.root, new_node)

class MyCalendar(object):
    def __init__(self):
        self.events = []

    def overlap(self, node1, node2):
        if node1[1] <= node2[0] or node2[1] <= node1[0]:
            return False
        return True

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for e in self.events:
            if self.overlap(e, (start, end)):
                return False
        self.events.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
assert obj.book(10, 20) == True
assert obj.book(15, 25) == False
assert obj.book(20, 30) == True
assert obj.book(20, 30) == False
assert obj.book(30, 50) == True
