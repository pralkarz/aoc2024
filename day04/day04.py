# TODO: For part 1, rather than brute-forcing, get matrices rotated by -45, 45, and 90 degrees,
# and do a simple substring search in them ("XMAS", "SAMX").

import re

from performance_utils.performance_utils import measure_performance

with open("day04/in04.txt") as in04:
    data = [row.strip() for row in in04.readlines()]


def part1(data):
    out = 0

    width = len(data[0])
    height = len(data)
    for y, row in enumerate(data):
        for x, letter in enumerate(row):
            if letter != "X":
                continue

            if y > 2:  # up
                if (
                    data[y - 1][x] == "M"
                    and data[y - 2][x] == "A"
                    and data[y - 3][x] == "S"
                ):
                    out += 1

            if y < height - 3:  # down
                if (
                    data[y + 1][x] == "M"
                    and data[y + 2][x] == "A"
                    and data[y + 3][x] == "S"
                ):
                    out += 1

            if x > 2:  # left
                if (
                    data[y][x - 1] == "M"
                    and data[y][x - 2] == "A"
                    and data[y][x - 3] == "S"
                ):
                    out += 1

            if x < width - 3:  # right
                if (
                    data[y][x + 1] == "M"
                    and data[y][x + 2] == "A"
                    and data[y][x + 3] == "S"
                ):
                    out += 1

            if x > 2 and y > 2:  # up-left
                if (
                    data[y - 1][x - 1] == "M"
                    and data[y - 2][x - 2] == "A"
                    and data[y - 3][x - 3] == "S"
                ):
                    out += 1

            if x < width - 3 and y < height - 3:  # down-right
                if (
                    data[y + 1][x + 1] == "M"
                    and data[y + 2][x + 2] == "A"
                    and data[y + 3][x + 3] == "S"
                ):
                    out += 1

            if x < width - 3 and y > 2:  # up-right
                if (
                    data[y - 1][x + 1] == "M"
                    and data[y - 2][x + 2] == "A"
                    and data[y - 3][x + 3] == "S"
                ):
                    out += 1

            if x > 2 and y < height - 3:  # down-left
                if (
                    data[y + 1][x - 1] == "M"
                    and data[y + 2][x - 2] == "A"
                    and data[y + 3][x - 3] == "S"
                ):
                    out += 1

    return out


def part1_regex(data):
    w = len(data[0])

    s = "\n".join(data)
    regexes = (
        ["(?=XMAS)", "(?=SAMX)"]
        + [f"(?=X.{{{w + x}}}M.{{{w + x}}}A.{{{w + x}}}S)" for x in [-1, 0, 1]]
        + [f"(?=S.{{{w + x}}}A.{{{w + x}}}M.{{{w + x}}}X)" for x in [-1, 0, 1]]
    )

    out = 0
    for regex in regexes:
        out += len(re.findall(regex, s, re.S))

    return out


def part2(data):
    out = 0

    for y, row in enumerate(data[1:-1], start=1):
        for x, letter in enumerate(row[1:-1], start=1):
            if letter != "A":
                continue

            uldr_diagonal = data[y - 1][x - 1] + "A" + data[y + 1][x + 1]
            dlur_diagonal = data[y + 1][x - 1] + "A" + data[y - 1][x + 1]

            if uldr_diagonal in ["MAS", "SAM"] and dlur_diagonal in ["MAS", "SAM"]:
                out += 1

    return out


def part2_regex(data):
    w = len(data[0])

    s = "\n".join(data)
    regexes = [
        f"(?={x[0]}[^\\n]{x[1]}.{{{w - 1}}}A.{{{w - 1}}}{x[2]}[^\\n]{x[3]})"
        for x in ("MSMS", "MMSS", "SMSM", "SSMM")
    ]

    out = 0
    for regex in regexes:
        out += len(re.findall(regex, s, re.S))

    return out


measure_performance("part 1", part1, data)
measure_performance("part 1 regex", part1_regex, data)
measure_performance("part 2", part2, data)
measure_performance("part 2 regex", part2_regex, data)
