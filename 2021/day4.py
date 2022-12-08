import sys

class Board:

    def __init__(self, board):
        # assume board is a 5x5 grid
        assert len(board) == 5
        for row in board:
            assert len(row) == 5, 'len of row is actually: ' + str(len(row))
        self.board = board

        self.marked = []
        for i in range(5):
            self.marked.append([False, False, False, False, False])

    def mark(self, num):
        for row in range(5):
            for col in range(5):
                print("row: " + str(row) + " col: " + str(col))
                if self.board[row][col] == num:
                    self.marked[row][col] = True

                    if self.isBingo(row, col):
                        return True
        return False

    def isBingo(self, row, col):
        # check entire row and col for bingo. used by mark.
        colBingo = True
        rowBingo = True
        for i in range(5):
            if not self.marked[i][col]:
                colBingo = False
            if not self.marked[row][i]:
                rowBingo = False

        return colBingo or rowBingo

    def getSumUnmarked(self):
        sumUnmarked = 0
        for row in range(5):
            for col in range(5):
                if not self.marked[row][col]:
                    sumUnmarked += self.board[row][col]
        return sumUnmarked

def getBingoScore(nums, boards):
    # once all boards are created, go through and mark nums.
    for num in nums:
        for i in range(len(boards)):
            board = boards[i]
            if board.mark(num):
                return board.getSumUnmarked() * num

    return -1

file = open('day4_input.txt', 'r')
lines = file.readlines()

order = [int(x) for x in lines[0].split(',')]

boards = []

curBoard = []
for i in range(2, len(lines)):
    lineSplit = lines[i].split()
    if len(curBoard) == 5:
        print(curBoard)
        boards.append(Board(curBoard))
        curBoard = []
        continue
    nums = [int(x) for x in lineSplit]
    curBoard.append(nums)

print(getBingoScore(order, boards))


