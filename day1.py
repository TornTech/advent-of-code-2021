from typing import List


def read_puzzle_input(path) -> List[int]:
    with open(path) as f:
        contents = [line.strip() for line in f]
    contents = [int(i) for i in contents]
    return contents


def part_one(data) -> int:
    increase_count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increase_count += 1
    return increase_count


def part_two(data):
    window_sum = 0
    increase_count = 0
    for (i, num) in enumerate(data):
        if i < 3:
            window_sum += num
        else:
            num1 = window_sum
            window_sum -= data[i-3]
            window_sum += data[i]
            num2 = window_sum
            if num2 > num1:
                increase_count += 1
    return increase_count


puzzle_input = read_puzzle_input("day1.txt")
print(f"Part one solution is {part_one(puzzle_input)}")
print(f"Part two solution is {part_two(puzzle_input)}")
