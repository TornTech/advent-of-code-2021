def read_puzzle_input(path) -> list:
    contents = []
    with open(path) as f:
        for line in f:
            coordinates = line.strip().split(" -> ")
            coordinates = [pair.split(",") for pair in coordinates]
            coordinates = [list(map(int, i)) for i in coordinates]
            contents.append(coordinates)
    return contents


def part_one(data) -> int:
    line_count = []
    for i in range(1000):
        line_count.append([0] * 1000)
    for line in data:
        x1 = line[0][0]; y1 = line[0][1]; x2 = line[1][0]; y2 = line[1][1]
        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            for i in range(start, end + 1):
                line_count[i][x1] += 1
        if y1 == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            for i in range(start, end + 1):
                line_count[y1][i] += 1
    return count_overlapping_lines(line_count)


def part_two(data) -> int:
    line_count = []
    for i in range(1000):
        line_count.append([0] * 1000)
    for line in data:
        x1 = line[0][0]; y1 = line[0][1]; x2 = line[1][0]; y2 = line[1][1]
        x_dir = 1 if x2 > x1 else -1 if x1 > x2 else 0
        y_dir = 1 if y2 > y1 else -1 if y1 > y2 else 0
        x_pos = x1
        y_pos = y1
        for _ in range(max(abs(x2-x1), abs(y2-y1)) + 1):
            line_count[y_pos][x_pos] += 1
            x_pos += x_dir
            y_pos += y_dir
    return count_overlapping_lines(line_count)


def count_overlapping_lines(line_count) -> int:
    max_count = 0
    for row in line_count:
        for col in row:
            if col >= 2:
                max_count += 1
    return max_count


puzzle_input = read_puzzle_input("day5.txt")
print(f"Part one solution is {part_one(puzzle_input)}")
print(f"Part two solution is {part_two(puzzle_input)}")
