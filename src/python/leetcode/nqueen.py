
def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    
    def is_safe(row, c):
        for prev_r in range(row):
            pc = board[prev_r]
            if pc == c:
                return False
            if abs(pc - c) == abs(prev_r - row):
                return False
        return True
        
    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return 
        for c in range(n):
            if (is_safe(row, c)):
                board[row] = c
                backtrack(row + 1)
                board[row] = -1
        return 
                
    backtrack(0)
    found = len(solutions) > 0
    if found:
        for sol in solutions:
            print(sol)
        print(f"Total solutions: {len(solutions)}")
        return
    print("Invalid Input")
    
    
if __name__ == "__main__":
    n = 4
    solve_n_queens(n)