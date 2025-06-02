def solveNQueens(n):
    def backtrack(row, diagonals, anti_diagonals, cols, state):
        if row == n:
            board = ["".join(r) for r in state]
            solutions.append(board)
            return

        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col

            if (col in cols or
                curr_diag in diagonals or
                curr_anti_diag in anti_diagonals):
                continue

            # Place queen
            state[row][col] = 'Q'
            cols.add(col)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)

            backtrack(row + 1, diagonals, anti_diagonals, cols, state)

            # Remove queen (backtrack)
            state[row][col] = '.'
            cols.remove(col)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)

    solutions = []
    empty_board = [["."] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return solutions
