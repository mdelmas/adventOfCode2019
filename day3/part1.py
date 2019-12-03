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

def findClosestIntersection(wire1, wire2):
    wire1Coords = computeCoordinates(wire1)
    wire2Coords = computeCoordinates(wire2)
    intersections = set(wire1Coords) & set(wire2Coords)
    closestIntersection = min(intersections, key=lambda c: abs(c.x) + abs(c.y))
    return closestIntersection

f = open("./input")
wire1 = [Path(d[0], int(d[1:])) for d in f.readline().split(',')]
wire2 = [Path(d[0], int(d[1:])) for d in f.readline().split(',')]

closestIntersection = findClosestIntersection(wire1, wire2)
print("Closest intersection distance is " + str(abs(closestIntersection.x) + abs(closestIntersection.y)))