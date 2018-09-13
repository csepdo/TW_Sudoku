import os
import sys


description = """This is a Sudoku game. The objective is to fill a 9×9
grid with digits so that each column, each row,
and each of the nine 3×3 boxes that compose
the grid contains all of the digits from 1 to 9.
To fill the board. you have to give the coordinates (row, column),
and the digit you want to enter (e.g.: 0 1 2).
If you want to delete a digit, you type 0 after the coordinates.
The coordinates 0 0 indicate the top left corner."""
col = 9
row = 9
e = ' '
board = [0] * col
for i in range(col):
    board[i] = [0] * row
solution = [0] * col
for j in range(col):
    solution[j] = [0] * row


def start():
    if len(sys.argv) == 1:
        filename = "easy_boards.txt"
        line_no = 0
    elif sys.argv[1] == "easy":
        filename = "easy_boards.txt"
        line_no = int(sys.argv[2])
    elif sys.argv[1] == "medium":
        filename = "medium_boards.txt"
        line_no = int(sys.argv[2])
    elif sys.argv[1] == "hard":
        filename = "hard_boards.txt"
        line_no = int(sys.argv[2])
    elif sys.argv[1] == "extreme":
        filename = "extreme_boards.txt"
        line_no = int(sys.argv[2])
    with open(filename, "r") as new_board:
        lines = new_board.readlines()
        imported_board = []
        board_lines = list(lines[line_no].split("#"))
        i = 0
        for line in board_lines:
            line = board_lines[i].split(",")
            line[-1] = line[-1].replace("\n", "")
            imported_board.append(line)
            i += 1
    board_format(imported_board)
    return imported_board


def board_format(board):
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[0]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[1]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[2]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[3]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[4]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[5]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[6]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[7]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('| | {} | {} | {} | | {} | {} | {} | | {} | {} | {} | |'.format(*board[8]))
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')
    print('+-+---+---+---+-+---+---+---+-+---+---+---+-+')


def modify_board():
    replace_number()
    os.system('cls' if os.name == 'nt' else 'clear')


def import_solution():
    if len(sys.argv) == 1:
        filename = "easy_boards.txt"
        line_no = 0
    elif sys.argv[1] == "easy":
        filename = "easy_boards.txt"
        line_no = int(sys.argv[2])
    elif sys.argv[1] == "medium":
        filename = "medium_boards.txt"
        line_no = int(sys.argv[2])
    elif sys.argv[1] == "hard":
        filename = "hard_boards.txt"
        line_no = int(sys.argv[2])
    elif sys.argv[1] == "extreme":
        filename = "extreme_boards.txt"
        line_no = int(sys.argv[2])
    with open(filename, "r") as new_solution:
        lines = new_solution.readlines()
        solution = []
        solution_lines = list(lines[line_no+1].split("#"))
        i = 0
        for line in solution_lines:
            line = solution_lines[i].split(",")
            line[-1] = line[-1].replace("\n", "")
            solution.append(line)
            i += 1
    return solution


def check_numbers(solved_board):
    if board == solution:
        print('Correct')


def replace_number():
    number_parameters = []
    number_parameters = [int(r) for r in input().split()]
    if number_parameters[2] == 0:
        board[number_parameters[0]][number_parameters[1]] = e
    elif str(number_parameters[2]) != solved_board[number_parameters[0]][number_parameters[1]]:
        print("Incorrect number!")
    elif board[number_parameters[0]][number_parameters[1]] == e:
        board[number_parameters[0]][number_parameters[1]] = number_parameters[2]


print(description)
board = start()
solved_board = import_solution()
while True:
    try:
        modify_board()
        board_format(board)
    except IndexError:
        print("Incorrect format.")
