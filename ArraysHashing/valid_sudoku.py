class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        l = []

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char != '.':
                    l.append((char, i))
                    l.append((j, char))
                    l.append((i // 3, j // 3, char))

        return len(l) == len(set(l))