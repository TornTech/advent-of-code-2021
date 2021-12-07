from typing import List
import statistics


def read_puzzle_input(path) -> List[int]:
    with open(path) as f:
        contents = [line.strip() for line in f]
        contents = [int(val) for val in contents[0].split(",")]
    return contents


def part_one(data: List[int]) -> int:
    median_pos = int(statistics.median(data))
    fuel_required = 0
    for crab_position in data:
        fuel_required += abs(median_pos - crab_position)
    return fuel_required


def part_two(data: List[int]) -> int:
    mean_pos = int(statistics.mean(data))
    fuel_required = 0
    for crab_position in data:
        fuel_required += sum([i for i in range(int(abs(mean_pos - crab_position)) + 1)])
    return fuel_required


puzzle_input = read_puzzle_input("day7.txt")
print(f"Part one solution is {part_one(puzzle_input)}")
print(f"Part two solution is {part_two(puzzle_input)}")
