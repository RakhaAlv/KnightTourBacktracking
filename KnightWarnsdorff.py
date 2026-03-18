import time
import os

N = 8 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board, pesan=""):
    clear_screen()
    print("=== Knight's Tour (Warnsdorff's) ===")
    print(f"Status: {pesan}\n")
    
    for i in range(N):
        for j in range(N):
            print(f"{board[i][j]:3}", end=' ')
        print()
    
    time.sleep(1)

def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def get_degree(board, x, y, move_x, move_y):
    count = 0
    for i in range(8):
        if is_safe(x + move_x[i], y + move_y[i], board):
            count += 1
    return count

def solve_kt_warnsdorff(x, y, pos, board, move_x, move_y):
    if pos == N**2:
        return True

    next_moves = []
    for i in range(8):
        nx = x + move_x[i]
        ny = y + move_y[i]
        if is_safe(nx, ny, board):
            degree = get_degree(board, nx, ny, move_x, move_y)
            next_moves.append((degree, nx, ny))

    next_moves.sort(key=lambda item: item[0])

    for degree, nx, ny in next_moves:
        board[nx][ny] = pos
        pesan_maju = f"Langkah ke-{pos} di ({nx}, {ny}) | Sisa jalan (Degree): {degree}"
        print_board(board, pesan_maju)

        if solve_kt_warnsdorff(nx, ny, pos + 1, board, move_x, move_y):
            return True

        board[nx][ny] = -1
        pesan_mundur = f"Buntu! Backtrack dari ({nx}, {ny}), hapus langkah ke-{pos}"
        print_board(board, pesan_mundur)

    return False

def solve_kt():
    board = [[-1 for _ in range(N)] for _ in range(N)]

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    start_x, start_y = 0, 0
    board[start_x][start_y] = 0
    
    print_board(board, f"Mulai dari posisi awal ({start_x}, {start_y})")
    
    if not solve_kt_warnsdorff(start_x, start_y, 1, board, move_x, move_y):
        print("\nSolusi tidak ditemukan!")
    else:
        print("\nSolusi Berhasil ditemukan!")

if __name__ == "__main__":
    solve_kt()