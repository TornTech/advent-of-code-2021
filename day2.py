from typing import List


def read_puzzle_input(path) -> List[tuple]:
    with open(path) as f:
        contents = [tuple(line.strip().split()) for line in f]
    return contents


def part_one(data) -> int:
    horizontal_position = 0
    depth = 0
    for move in data:
        move_type = move[0]
        move_amount = int(move[1])
        if move_type == 'forward':
            horizontal_position += move_amount
        elif move_type == "up":
            depth -= move_amount
        else:
            depth += move_amount
    return horizontal_position * depth


def part_two(data) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0
    for move in data:
        move_type = move[0]
        move_amount = int(move[1])
        if move_type == 'forward':
            horizontal_position += move_amount
            depth += aim * move_amount
        elif move_type == "up":
            aim -= move_amount
        else:
            aim += move_amount
    return horizontal_position * depth


puzzle_input = read_puzzle_input("day2.txt")
print(f"Part one solution is {part_one(puzzle_input)}")
print(f"Part two solution is {part_two(puzzle_input)}")
