from collections import namedtuple


Coord = namedtuple('Coord', 'x y')
Path = namedtuple('Path', 'direction length')


def computeCoordinates(wire):
    coords = []
    current = Coord(0, 0)
    for path in wire:
        for i in range(0, path.length):
            if path.direction == 'R':
                current = Coord(current.x + 1, current.y)
            elif path.direction == 'L':
                current = Coord(current.x - 1, current.y)
            elif path.direction == 'U':
                current = Coord(current.x, current.y + 1)
            elif path.direction == 'D':
                current = Coord(current.x, current.y - 1)
            coords.append(current)
    return coords

def findFewestStepsToIntersection(wire1, wire2):
    wire1Coords = computeCoordinates(wire1)
    wire2Coords = computeCoordinates(wire2)
    intersections = set(wire1Coords) & set(wire2Coords)
    intersection = min(intersections, key=lambda c: wire1Coords.index(c)+1 + wire2Coords.index(c)+1)
    return wire1Coords.index(intersection)+1 + wire2Coords.index(intersection)+1

f = open("./input")
wire1 = [Path(d[0], int(d[1:])) for d in f.readline().split(',')]
wire2 = [Path(d[0], int(d[1:])) for d in f.readline().split(',')]

fewestStepsToIntersection = findFewestStepsToIntersection(wire1, wire2)
print("Fewest steps to intersection is " + str(fewestStepsToIntersection))