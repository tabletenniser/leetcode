"""
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
    Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

    Example:

        StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

        iterator.next(); // return 'L'
        iterator.next(); // return 'e'
        iterator.next(); // return 'e'
        iterator.next(); // return 't'
        iterator.next(); // return 'C'
        iterator.next(); // return 'o'
        iterator.next(); // return 'd'
        iterator.hasNext(); // return true
        iterator.next(); // return 'e'
        iterator.hasNext(); // return false
        iterator.next(); // return ' '
"""
class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.string = compressedString
        self.cur_index = 0
        self.hasNextCh = True
        self.cur_char = ' '
        i = 0
        if self.cur_index+i+1 >= len(self.string):
            self.hasNextCh = False
            return None

        while self.cur_index+i+1 < len(self.string) and self.string[self.cur_index+i+1] >= '0' and self.string[self.cur_index+i+1] <= '9':
            i += 1
        self.cur_char = self.string[self.cur_index]
        counter_str = self.string[self.cur_index+1:self.cur_index+i+1]
        self.cur_index += i+1
        self.cur_count = int(counter_str)
        return None

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNextCh:
            return ' '
        if self.cur_count == 0:
            i = 0
            while self.cur_index+i+1 < len(self.string) and self.string[self.cur_index+i+1] >= '0' and self.string[self.cur_index+i+1] <= '9':
                i += 1
            self.cur_char = self.string[self.cur_index]
            counter_str = self.string[self.cur_index+1:self.cur_index+i+1]
            self.cur_index += i+1
            self.cur_count = int(counter_str)
        self.cur_count -= 1
        if self.cur_index+1 >= len(self.string) and self.cur_count == 0:
            self.hasNextCh = False
        return self.cur_char

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasNextCh
