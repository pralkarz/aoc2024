from performance_utils.performance_utils import measure_performance

with open("day25/in25.txt") as in25:
    data = in25.read().strip()


def part1(data):
    schematics = [schematic.split("\n") for schematic in data.split("\n\n")]
    width = len(schematics[0][0])
    height = len(schematics[0]) - 2  # topmost and bottommost rows don't count

    locks = []
    keys = []
    for schematic in schematics:
        first_tile = schematic[0][0]
        counts = []
        for x in range(width):
            count = 0
            while schematic[count + 1][x] == first_tile:
                count += 1

            match first_tile:
                case "#":
                    counts.append(count)
                case ".":
                    counts.append(height - count)
        match first_tile:
            case "#":
                locks.append(counts)
            case ".":
                keys.append(counts)

    out = 0
    for lock in locks:
        for key in keys:
            for i in range(len(key)):
                if lock[i] + key[i] > height:
                    break
            else:
                out += 1

    return out


measure_performance("part 1", part1, data)
