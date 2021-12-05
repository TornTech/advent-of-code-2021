draw_numbers = []
bingo_boards = []
completed_boards = set()


def read_puzzle_input(path) -> None:
    with open(path) as f:
        contents = [line.strip() for line in f]
    global draw_numbers
    draw_numbers = [int(val) for val in contents[0].split(",")]

    global bingo_boards
    contents = contents[2:]
    current_board = []
    for index, line in enumerate(contents):
        if line != "":
            line_array = [[int(val), False] for val in list(filter(lambda val: val != "", line.split(" ")))]
            current_board.append(line_array)
            if index == len(contents) - 1:
                bingo_boards.append(current_board)
                current_board = []
        else:
            bingo_boards.append(current_board)
            current_board = []


def part_one() -> int:
    for curr_number in draw_numbers:
        for bingo_board in bingo_boards:
            update_bingo_board(bingo_board, curr_number)
            if is_bingo(bingo_board):
                return calculate_unmarked_numbers(bingo_board) * curr_number
    return -1


def part_two() -> int:
    global bingo_boards
    for curr_number in draw_numbers:
        for index, bingo_board in enumerate(bingo_boards):
            if not (index in completed_boards):
                update_bingo_board(bingo_board, curr_number)
                if is_bingo(bingo_board):
                    if len(completed_boards) == len(bingo_boards) - 1:
                        return calculate_unmarked_numbers(bingo_boards[index]) * curr_number
                    else:
                        completed_boards.add(index)
    return -1


def calculate_unmarked_numbers(bingo_board) -> int:
    unmarked_sum = 0
    for line in bingo_board:
        for pair in line:
            if not pair[1]:
                unmarked_sum += pair[0]
    return unmarked_sum


def is_bingo(bingo_board, ) -> bool:
    for i in range(5):
        if bingo_board[0][i][1] or bingo_board[i][0][1]:
            for j in range(1, 5):
                if not bingo_board[j][i][1]:
                    break
                elif j == 4 and bingo_board[j][i][1]:
                    return True
        if bingo_board[i][0][1]:
            for j in range(1, 5):
                if not bingo_board[i][j][1]:
                    break
                elif j == 4 and bingo_board[i][j][1]:
                    return True
    return False


def update_bingo_board(bingo_board, drawn_number) -> None:
    for line in bingo_board:
        for pair in line:
            if pair[0] == drawn_number:
                pair[1] = True


read_puzzle_input("day4.txt")
print(f"Part one solution is {part_one()}")
print(f"Part two solution is {part_two()}")
