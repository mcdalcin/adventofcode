import sys

class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def containsPoint(self, x, y):
        # vertical
        if self.x1 == self.x2:
            # y needs to be btwn y1 and y2
            return (y >= self.y1 and y <= self.y2) or (y <= self.y1 and y >= self.y2)

        # horizontal
        if self.y1 == self.y2:
            return (x >= self.x1 and x <= self.x2) or (x <= self.x1 and y >= self.x2)

    def incrementPoints(self, points):
        if self.x1 == self.x2:
            # vertical line, increment all points x1, y1 -> y2 or y2 -> y1
            if self.y1 <= self.y2:
                minY = self.y1
                maxY = self.y2
            else:
                minY = self.y2
                maxY = self.y1

            for i in range(minY, maxY + 1):
                points[i][self.x1] += 1
        elif self.y1 == self.y2:
            if self.x1 <= self.x2:
                minX = self.x1
                maxX = self.x2
            else:
                minX = self.x2
                maxX = self.x1

            for i in range(minX, maxX + 1):
                points[self.y1][i] += 1
        else:
            # diagonal line.. 45 degrees
            curX = self.x1
            curY = self.y1
            while curX != self.x2 and curY != self.y2:
                # add curX and curY
                points[curY][curX] += 1

                if curX > self.x2:
                    curX -= 1
                else:
                    curX += 1

                if curY > self.y2:
                    curY -= 1
                else:
                    curY += 1
            #finally add final pt
            points[curY][curX] += 1



file = open('day5_input.txt', 'r')
fileLines = file.readlines()

lines = []

for l in fileLines:
    split = l.split()
    split1 = [int(x) for x in split[0].split(',')]
    split2 = [int(x) for x in split[2].split(',')]

    # check if horizontal or vertical
    lines.append(Line(split1[0],split2[0],split1[1],split2[1]))

numOverlap = 0

overlapPoints = []
for i in range(1000):
    overlapPoints.append([0] * 1000)

for line in lines:
    line.incrementPoints(overlapPoints)

for row in range(1000):
    for col in range(1000):
        if overlapPoints[row][col] >= 2:
            numOverlap += 1

print(numOverlap)

