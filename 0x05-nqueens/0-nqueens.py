#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, col):
    if col >= N:
        print_solution(board)
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0  # Backtrack if placing the queen here doesn't lead to a solution
    return res

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens_util(board, 0):
        print("No solution exists")
        return False

def print_solution(board):
    solutions = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solutions.append([i, j])
    print(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(N)

