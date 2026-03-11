# CSIT 461- Intro to AI/Knowledge Engineering
# Shahin Mehdipour Ataee
# SUNY Fredonia
# Spring 2026

# Assignment #3- N-Queens Problem: Hill Climbing Algorithm
# Aaron Burkett
# 3/11/2026

import random
import copy

N = 8
SIDEWAYS_LIMIT = 100


def showState(state):
    for row in state['board']:
        for col in row:
            print(col, end=' ')
        print()
    print()


def randomState():
    state = {
        'board': [['-' for _ in range(N)] for _ in range(N)]
    }

    for col in range(N):
        row = random.randint(0, N-1)
        state['board'][row][col] = 'Q'

    return state


def getQueens(state):

    queens = []

    for col in range(N):
        for row in range(N):
            if state['board'][row][col] == 'Q':
                queens.append((row, col))

    return queens


def areAttacking(q1, q2):

    qR, qC = q1
    oR, oC = q2

    # same row
    if qR == oR:
        return True

    # diagonal
    if abs(qR - oR) == abs(qC - oC):
        return True

    return False


def heuristic(state):

    queens = getQueens(state)
    attacks = 0

    for i in range(len(queens)-1):
        for j in range(i+1, len(queens)):
            if areAttacking(queens[i], queens[j]):
                attacks += 1

    return attacks


def generateNeighbors(state):

    neighbors = []

    for col in range(N):

        currentRow = None

        for row in range(N):
            if state['board'][row][col] == 'Q':
                currentRow = row
                break

        for row in range(N):

            if row != currentRow:

                child = copy.deepcopy(state)

                child['board'][currentRow][col] = '-'
                child['board'][row][col] = 'Q'

                neighbors.append(child)

    return neighbors


def hillClimb():

    current = randomState()
    sidewaysMoves = 0

    while True:

        currentH = heuristic(current)

        if currentH == 0:
            return current

        neighbors = generateNeighbors(current)

        bestNeighbor = None
        bestH = float('inf')

        for n in neighbors:
            
            # Heuristic = Number of attacking queen pairs
            h = heuristic(n)

            if h < bestH:
                bestNeighbor = n
                bestH = h

        if bestH > currentH:
            return None

        if bestH == currentH:
            sidewaysMoves += 1
            if sidewaysMoves > SIDEWAYS_LIMIT:
                return None
        else:
            sidewaysMoves = 0

        current = bestNeighbor


def solve():

    if N < 4:
        print("No solution exists for this value of N")
        return

    restartCount = 0

    while True:

        solution = hillClimb()

        if solution is not None:
            print("Solution found after", restartCount, "random restarts!\n")
            showState(solution)
            return

        restartCount += 1


solve()