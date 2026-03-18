import time
import os

N = 5 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board, pesan=""):
    clear_screen()
    print(f"===Algoritma Backtracking: Knight's Tour Problem===")
    print(f"Status: {pesan}\n") 
    
    for i in range(N):
        for j in range(N):
            print(f"{board[i][j]:2}", end=' ')
        print()
    
    time.sleep(1) 

def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def solve_kt_util(x, y, pos, board, move_x, move_y):
    if pos == N**2:
        return True

    for i in range(8):
        new_x = x + move_x[i]
        new_y = y + move_y[i]

        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = pos
            pesan_maju = f"Pilih langkah ke-{pos} di koordinat ({new_x}, {new_y})"
            print_board(board, pesan_maju)

            if solve_kt_util(new_x, new_y, pos + 1, board, move_x, move_y):
                return True

            board[new_x][new_y] = -1
            pesan_mundur = f"Jalan Buntu! Backtrack dari ({new_x}, {new_y}), hapus langkah ke-{pos}"
            print_board(board, pesan_mundur)

    return False

def solve_kt():
    board = [[-1 for _ in range(N)] for _ in range(N)]

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    start_x, start_y = 0, 0
    board[start_x][start_y] = 0
    
    print_board(board, f"Mulai dari posisi awal ({start_x}, {start_y})")
    
    if not solve_kt_util(start_x, start_y, 1, board, move_x, move_y):
        print("\nSolusi tidak ditemukan!")
    else:
        print("\nSolusi Berhasil ditemukan!")

if __name__ == "__main__":
    solve_kt()
