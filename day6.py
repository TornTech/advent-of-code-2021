from typing import List


def read_puzzle_input(path) -> List[int]:
    with open(path) as f:
        contents = [line.strip() for line in f]
        contents = [int(val) for val in contents[0].split(",")]
    return contents


def part_one(data: List[int]) -> int:
    return fish_counter(data, 80)


def part_two(data: List[int]) -> int:
    return fish_counter(data, 256)


def fish_counter(data: List[int], days: int) -> int:
    fish_counter_dict = setup_dict(data)
    for _ in range(days):
        fish_counter_dict = update_dict(fish_counter_dict)
    return sum(fish_counter_dict.values())


def update_dict(dictionary: dict):
    new_dictionary = dict()
    new_born_babies = dictionary.get(0, 0)
    for i in range(8):
        new_dictionary[i] = dictionary.get(i + 1, 0)
    new_dictionary[8] = new_born_babies
    new_dictionary[6] = new_dictionary.get(6, 0) + new_born_babies
    return new_dictionary


def setup_dict(arr: list):
    fish_counter_dict = dict()
    for val in arr:
        fish_counter_dict[val] = fish_counter_dict.get(val, 0) + 1
    return fish_counter_dict


puzzle_input = read_puzzle_input("day6.txt")
print(f"Part one solution is {part_one(puzzle_input)}")
print(f"Part two solution is {part_two(puzzle_input)}")
