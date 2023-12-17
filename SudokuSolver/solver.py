
sample_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

BOARD_SIZE = 9


def solve(bo):
    find = find_empty(bo)

    if not find:
        # found solution
        return True
    else:
        row, col = find

    for i in range(1, BOARD_SIZE + 1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # recursively try to solve with new value added
            if solve(bo):
                return True
            # last element wasn't correct, reset it back to 0
            bo[row][col] = 0

    return False

# def solve(bo):
#     stack = []
#     pos = find_empty(bo)
#
#     if not pos:
#         return True  # Board is already complete
#
#     stack.append((pos, 0))  # Initial position and starting number
#
#     while stack:
#         (row, col), num = stack.pop()
#
#         if num != 0:  # If backtracking, reset current cell to 0 before trying next number
#             bo[row][col] = 0
#
#         for i in range(num + 1, 10):  # Start from the next number after the current num
#             if valid(bo, i, (row, col)):
#                 bo[row][col] = i
#                 next_pos = find_empty(bo)
#
#                 if not next_pos:  # Solution found
#                     return True
#
#                 stack.append(((row, col), i))  # Push current position and number
#                 stack.append((next_pos, 0))   # Push next position and start number
#                 break
#         else:
#             # No valid number found, continue to backtrack
#             continue
#
#     return False


# Check to see if placing a number at a certain position on the board is valid
# pos - tuple; pos[0] = row index; pos[1] = column index
def valid(bo, num, pos):

    # check row
    for i in range(len(bo[0])):
        # check to see if number already present in row but ignore current pos
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box using integer division
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            # print(len(board))
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    # rows
    for i in range(len(bo)):
        # columns
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None

print_board(sample_board)
solve(sample_board)
print("_________________________")
print_board(sample_board)
