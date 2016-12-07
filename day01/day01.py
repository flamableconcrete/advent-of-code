import csv


NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4


class Player(object):

    def __init__(self, name):
        self.name = name
        self.facing = NORTH
        self.x = 0
        self.y = 0

    def __str__(self):
        return "%s is at X: %s, Y: %s" % (self.name, self.x, self.y)

    def find_endpoint(self, directions):
        for step in directions:
            direction_to_turn = step[0:1]
            distance = int(step[1:])
            self.rotate(direction_to_turn)
            self.move(distance)

    def rotate(self, direction_to_turn):
        if direction_to_turn == "R":
            self.facing = self.facing + 1
        else:
            self.facing = self.facing - 1
        if self.facing == 0:
            self.facing = WEST
        if self.facing == 5:
            self.facing = NORTH

    def move(self, distance):
        if self.facing == NORTH:
            self.y = self.y + distance
        elif self.facing == EAST:
            self.x = self.x + distance
        elif self.facing == SOUTH:
            self.y = self.y - distance
        elif self.facing == WEST:
            self.x = self.x - distance
        else:
            print("You done screwed up somewhere!")

def main():
    directions = []

    with open("input.csv") as csvfile:
        for row in csv.reader(csvfile):
            for item in row:
                directions.append(item.strip())

    #directions = ["R5", "L5", "R5", "R3"]

    playerOne = Player("flamableconcrete")

    playerOne.find_endpoint(directions)

    print(playerOne)

    blocks_away = abs(playerOne.x) + abs(playerOne.y)

    print("The Easter Bunny HQ is %s blocks away" % (blocks_away))


if __name__ == "__main__":
    main()