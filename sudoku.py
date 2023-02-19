import copy
import time

depth = 0


def get_sudoku():
    filename = "sudoku_input.txt"
    with open(filename, "r") as file:
        starting = file.read().split("\n")
    for r, row in enumerate(starting):
        temp_row = ""
        for cell in row:
            if cell.isdigit():
                temp_row += cell
        starting[r] = temp_row

    return starting


def check_rules(b):
    # False if invalid board

    # Rows
    for row in b:
        for i in range(1, 10):
            if row.count(str(i)) > 1:
                # print("rows")
                return False

    # Columns
    for column_index in range(len(b[0])):
        column = list(row[column_index] for row in b)
        for i in range(1, 10):
            if column.count(str(i)) > 1:
                # print("columns")
                return False

    # Squares
    for row in (0, 3, 6):
        for column in (0, 3, 6):
            square = []
            for r in range(0, 3):
                for c in range(0, 3):
                    if b[row + r][column + c] != "0" and b[row + r][column + c] in square:
                        # print("square")
                        # print(b[row + r][column + c])
                        return False
                    square.append(b[row + r][column + c])
    return True


def print_board(b):
    for r, row in enumerate(b):
        for i in (0, 3, 6):
            print(row[i:i + 3], end=" ")
        print()
    print()


def solve(b):
    global depth
    # print("#"*depth)
    if not check_rules(b):
        return False
    zeros = 0
    for r, row in enumerate(b):
        for c, cell in enumerate(row):
            if cell == "0":
                zeros += 1
                for i in range(1, 10):
                    new_board = copy.deepcopy(b)
                    new_board[r] = b[r][0:c] + str(i) + b[r][c + 1:]
                    if check_rules(new_board):
                        depth += 1
                        if solve(new_board):
                            return True
                        depth -= 1
                return
    if zeros == 0:
        print("SOLVED:")
        print_board(b)
        return True


def main():
    board = get_sudoku()
    print_board(board)
    if not check_rules(board):
        print("Invalid board provided.")
        exit()

    print("Board is valid.")
    print("Attempting to solve.\n")
    starting_time = time.time()
    solve(board)
    print("Time to solve:", time.time() - starting_time)


if __name__ == "__main__":
    main()
