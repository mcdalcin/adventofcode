from collections import Counter
from line_profiler_pycharm import profile
from copy import copy, deepcopy
from pandas import DataFrame
import pandas
import sys
import time
from heapq import *
import numpy as np
import math

file = open('day18_input.txt', 'r')
file_lines = [x.strip() for x in file.readlines()]

# every snailfish number is a pair, an ordered list of two elements. Each element
# of the pair can either be a regular number or another pair.

# To add two, form a pair from left and right parameters of the addition operatior.
#[1,2] + [[3,4],5] becomes [1,2],[[3,4],5]]

# musts reduce snailfish number
# if any pair is nested inside four pairs, the leftmost usch pair explodes
# if any regular number is 10 or greater, the leftmost such regular number splits.

# to explode a pair, pair's left value is added to the first regular number to the left of the exploding pair (if any)
# the pair's right value is added to the first regular number to the right of the exploding pair (if any).
# entire exploding pair is replaced with the regular number 0

# [[[[[9,8],1],2],3],4] ->
# [[[[0, 9],2,3,4]

# to split.. replace it with a pair;
# left -> # / 2 and rounded ddown
# right -> # / 2 and rounded up

# assume all are

# adding up a list of snailfish numbers...
# magnitude of the final sum.. magnitude is 3 times the magnitude of its left element plus 2 times the magnitude of its right element.
# magnitude of regular number is just that number

# build data struct to hold pairs..


class Number:
    def __init__(self, num):
        self.num = num


class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def tostring(self):
        return '[' + self.tostring_helper(self.left) + ', ' + self.tostring_helper(self.right) + ']'

    def tostring_helper(self, node):
        if isinstance(node, Number):
            return str(node.num)

        return '[' + self.tostring_helper(node.left) + ', ' + self.tostring_helper(node.right) + ']'

def createPair(string, currIndex):
    # look for next pair start..
    while string[currIndex] != '[' and not string[currIndex].isdigit():
        currIndex += 1

    if string[currIndex].isdigit():
        return Number(int(string[currIndex])), currIndex + 1

    if string[currIndex] != '[':
        return None

    leftPair, leftIndex = createPair(string, currIndex + 1)
    rightPair, rightIndex = createPair(string, leftIndex)

    return Pair(leftPair, rightPair), rightIndex

def calcMagnitude(pairTree):
    # check left and right and add up all

    if pairTree is None:
        return 0

    if isinstance(pairTree, Number):
        return pairTree.num

    return 3 * calcMagnitude(pairTree.left) + 2 * calcMagnitude(pairTree.right)


# [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]

def addPairs(pairA, pairB):
    newPair = Pair(pairA, pairB)
    #print('adding pairs:' + newPair.tostring())
    # explode, split, repeat..
    while True:
        # if we can explode, explode
        if explode(newPair):
            #print('after explode: ' + newPair.tostring())
            continue
        if split(newPair, None):
            #print('after split: ' + newPair.tostring())
            continue
        return newPair

recentEncounteredNum = None
def explode(pair):
    global recentEncounteredNum
    recentEncounteredNum = None
    return explode_helper(pair, 0)[0]


def explode_helper(pair, count):
    global recentEncounteredNum
    # traverse..
    if isinstance(pair, Number):
        recentEncounteredNum = pair
        return False, ()
    if count > 4:
        print('wtf > 3')
    if count == 4:
        # explode.
        if not isinstance(pair.left, Number) or not isinstance(pair.right, Number):
            print('wtf???')
            return False, ()
        return True, (pair.left, pair.right)

    exploded = None
    pairToAdd = None
    if pair.left is not None:
        exploded, pairToAdd = explode_helper(pair.left, count + 1)

        if exploded and len(pairToAdd) == 2:
            # immediately returned, remove pair.left
            pair.left = Number(0)

            if isinstance(recentEncounteredNum, Number):
                recentEncounteredNum.num += pairToAdd[0].num

            # add to right num,
            # pair.right.left.left...
            rightNumPair = pair.right
            # should not be None.
            while not isinstance(rightNumPair, Number):
                rightNumPair = rightNumPair.left
            rightNumPair.num += pairToAdd[1].num

            return exploded, ()

        if exploded and len(pairToAdd) == 1:
            # traverse pair.right ...
            rightPair = pair.right
            while not isinstance(rightPair, Number):
                rightPair = rightPair.left
            rightPair.num += pairToAdd[0].num

            return exploded, ()

        if exploded and len(pairToAdd) == 0:
            return exploded, pairToAdd

    if pair.right is not None:
        exploded, pairToAdd = explode_helper(pair.right, count + 1)

        if not exploded and len(pairToAdd) == 1:
            return exploded, pairToAdd
        if exploded and len(pairToAdd) == 2:
            # immediately returned, remove pair.left
            pair.right = Number(0)

            if isinstance(recentEncounteredNum, Number):
                recentEncounteredNum.num += pairToAdd[0].num

            return exploded, (pairToAdd[1],)

        if exploded and len(pairToAdd) == 0:
            return exploded, pairToAdd

    return exploded, pairToAdd


def split(pair, fromPair):
    # in order search pair..
    if isinstance(pair, Number):
        if pair.num >= 10:
            div = float(pair.num) / 2.0
            if fromPair.left == pair:
                fromPair.left = Pair(Number(math.floor(div)), Number(math.ceil(div)))
            else:
                fromPair.right = Pair(Number(math.floor(div)), Number(math.ceil(div)))
            return True
        else:
            return False

    return split(pair.left, pair) or split(pair.right, pair)

pairs = []
for line in file_lines:
    pairs.append(createPair(line, 0)[0])

maxMagnitude = 0
for i in range(len(file_lines)):
    for j in range(len(file_lines)):
        pairA = createPair(file_lines[i], 0)[0]
        pairB = createPair(file_lines[j], 0)[0]
        addedPair = addPairs(pairA, pairB)
        maxMagnitude = max(calcMagnitude(addedPair), maxMagnitude)

print(maxMagnitude)