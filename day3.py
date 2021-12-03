from typing import List


def read_puzzle_input(path) -> List[str]:
    with open(path) as f:
        contents = [line.strip() for line in f]
    return contents


def part_one(data) -> int:
    bit_count = len(data[0])
    count_zero = [0] * bit_count
    count_one = [0] * bit_count
    for line in data:
        for idx, num in enumerate(line):
            if num == '0':
                count_zero[idx] += 1
            else:
                count_one[idx] += 1

    gamma_rate_arr = []
    epsilon_rate_arr = []
    for i in range(bit_count):
        if count_one[i] > count_zero[i]:
            gamma_rate_arr.append("1")
            epsilon_rate_arr.append("0")
        else:
            gamma_rate_arr.append("0")
            epsilon_rate_arr.append("1")

    gamma_rate = int("".join(gamma_rate_arr), 2)
    epsilon_rate = int("".join(epsilon_rate_arr), 2)
    return gamma_rate * epsilon_rate


def part_two(data) -> int:
    oxygen_rating = int(generate_rating(data, 0, "oxygen"), 2)
    co2_rating = int(generate_rating(data, 0, "co2"), 2)
    return oxygen_rating * co2_rating


def generate_rating(data, index, generator_type) -> str:
    if len(data) == 1 or index >= len(data[0]):
        return data[0]

    least_common_bit = most_common_bit_at_index(data, index, generator_type)
    data = remove_least_common_bit(data, index, least_common_bit)
    return generate_rating(data, index + 1, generator_type)


def remove_least_common_bit(data, index, bit) -> List[str]:
    new_data = []
    for line in data:
        if line[index] == bit:
            new_data.append(line)
    return new_data


def most_common_bit_at_index(data, index, generator_type) -> str:
    count_zero = 0
    count_one = 0
    for line in data:
        if line[index] == '0':
            count_zero += 1
        else:
            count_one += 1

    if generator_type == "oxygen":
        return '1' if count_one >= count_zero else '0'
    else:
        return '0' if count_one >= count_zero else '1'


puzzle_input = read_puzzle_input("day3.txt")
print(f"Part one solution is {part_one(puzzle_input)}")
print(f"Part two solution is {part_two(puzzle_input)}")
