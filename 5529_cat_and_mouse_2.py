'''
A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a grid of size rows x cols, where each element is a wall, floor, player (Cat, Mouse), or food.

Players are represented by the characters 'C'(Cat),'M'(Mouse).
Floors are represented by the character '.' and can be walked on.
Walls are represented by the character '#' and cannot be walked on.
Food is represented by the character 'F' and can be walked on.
There is only one of each character 'C', 'M', and 'F' in grid.
Mouse and Cat play according to the following rules:

Mouse moves first, then they take turns to move.
During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the grid.
catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
Staying in the same position is allowed.
Mouse can jump over Cat.
The game can end in 4 ways:

If Cat occupies the same position as Mouse, Cat wins.
If Cat reaches the food first, Cat wins.
If Mouse reaches the food first, Mouse wins.
If Mouse cannot get to the food within 1000 turns, Cat wins.
Given a rows x cols matrix grid and two integers catJump and mouseJump, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.

Example 1:
Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
Output: true
Explanation: Cat cannot catch Mouse on its turn nor can it get the food before Mouse.

Example 2:
Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
Output: true
Example 3:

Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
Output: false
Example 4:

Input: grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
Output: false
Example 5:
Input: grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
Output: true

Constraints:

rows == grid.length
cols = grid[i].length
1 <= rows, cols <= 8
grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
There is only one of each character 'C', 'M', and 'F' in grid.
1 <= catJump, mouseJump <= 8
'''
class Solution:
    def isValidLocation(self, grid, new_location):
        x,y = new_location
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '#':
            return False
        return True

    def miniMax(self, grid, mouseMove, turn):
        gridStr = ' '.join(map(''.join, grid))
        print(self.mouse, self.cat, self.food, gridStr, turn)
        if self.mouse == self.cat or turn >= 72 or self.cat == self.food:
            return -1
        if self.mouse == self.food:
            return 1
        assert(grid[self.mouse[0]][self.mouse[1]] == 'M')
        assert(grid[self.cat[0]][self.cat[1]] == 'C')
        animal = 'mouse' if mouseMove else 'cat'
        if (gridStr, mouseMove, turn) in self.ht:
            print("cache hit: ", gridStr, mouseMove, self.ht[(gridStr, mouseMove, turn)])
            return self.ht[(gridStr, mouseMove, turn)]
        maxStep = self.mj if mouseMove else self.cj
        prevLoc = self.mouse if mouseMove else self.cat
        res = -1
        # self.ht[(gridStr, mouseMove)] = res
        for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
            for step in range(1, maxStep+1):
                new_location = (prevLoc[0] + x * step, prevLoc[1] + y * step)
                if not self.isValidLocation(grid, new_location):
                    break
                prevVal = grid[new_location[0]][new_location[1]]
                grid[new_location[0]][new_location[1]] = 'M' if mouseMove else 'C'
                grid[prevLoc[0]][prevLoc[1]] = '.'
                print(animal, " moves to - ", new_location)
                if mouseMove:
                    self.mouse = new_location
                    res = self.miniMax(grid, not mouseMove, turn + 1)
                    self.mouse = prevLoc
                    if res == 1:
                        print("mouse wins: ", gridStr, turn)
                        self.ht[(gridStr, mouseMove, turn)] = res
                        grid[new_location[0]][new_location[1]] = prevVal
                        grid[prevLoc[0]][prevLoc[1]] = 'M' if mouseMove else 'C'
                        return res
                else:
                    self.cat = new_location
                    res = self.miniMax(grid, not mouseMove, turn + 1)
                    self.cat = prevLoc
                    if res == -1:
                        print(turn, "mouse losses: ", gridStr)
                        grid[new_location[0]][new_location[1]] = prevVal
                        grid[prevLoc[0]][prevLoc[1]] = 'M' if mouseMove else 'C'
                        self.ht[(gridStr, mouseMove, turn)] = res
                        return res
                grid[new_location[0]][new_location[1]] = prevVal
                grid[prevLoc[0]][prevLoc[1]] = 'M' if mouseMove else 'C'
        print(turn, animal+" tried all possi: ", gridStr)
        # res = False if mouseMove else True
        self.ht[(gridStr, mouseMove, turn)] = res
        return res

    def canMouseWin(self, grid, catJump: int, mouseJump: int) -> bool:
        new_grid = []
        for row in grid:
            new_grid.append(list(row))
        self.cj = catJump
        self.mj = mouseJump
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell == 'C':
                    self.cat = (i, j)
                elif cell == 'M':
                    self.mouse = (i, j)
                elif cell == 'F':
                    self.food = (i, j)
        self.ht = {}
        res = self.miniMax(new_grid, True, 0)
        assert(res != 0)
        return True if res == 1 else False

s = Solution()
grid = ["####F","#C...","M...."] # True
catJump = 1
mouseJump = 2
grid = ["M.C...F"]
catJump = 1
mouseJump = 4
grid = ["M.C...F"] # False
catJump = 1
mouseJump = 3
grid = ["C...#","...#F","....#","M...."]
catJump = 2
mouseJump = 5
grid = [".M...","..#..","#..#.","C#.#.","...#F"] # True
catJump = 3
mouseJump = 1
grid=["CM..", "###.", "....", "F###"] # True
catJump=1
mouseJump=1
grid=[".C",".F","#.","M#"]
catJump=2
mouseJump=1
grid=["M....C","....#.","#..#..","#..#F.","..#...","#....."]
catJump=3
mouseJump=3
print(s.canMouseWin(grid, catJump, mouseJump))
