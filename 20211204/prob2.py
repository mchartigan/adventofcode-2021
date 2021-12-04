'''
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
'''

import re

class Board:
    def __init__(self, board):
        self.board = board
        self.checked = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.hasWon = False

    def checkNum(self, num):
        for i in range(0,5):
            for j in range(0,5):
                if self.board[i][j] == num:
                    self.checked[i][j] = 1

        for i in range(0,5):
            if sum(self.checked[i]) == 5:
                return True
            elif sum([row[i] for row in self.checked]) == 5:
                return True
        return False

    def sum(self):
        total = 0
        for i in range(0,5):
            for j in range(0,5):
                if not self.checked[i][j]:
                    total += int(self.board[i][j])

        return total

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [x.strip() for x in file.readlines()]
        
        nums = lines[0].split(',')

        i = 0
        board = [0]*5
        boards = []
        for line in lines[1:len(lines)]:
            if line == '':
                if i == 5:
                    boards.append(Board(board))
                board = [0]*5
                i = 0
            elif i < 5:
                board[i] = re.split(r" {1,}", line)
                i += 1
            else:
                i = 0

        winner = None
        finalnum = 0
        for num in nums:
            for board in boards:
                if board.hasWon == False and board.checkNum(num):
                    board.hasWon = True
                    winner = board
                    finalnum = num

        val = winner.sum()
        print(winner.sum() * int(finalnum))





