import random
import copy

N = 8

def randomState():
    state = {
        'board': [['-' for _ in range(N)] for _ in range(N)]
    }

    for col in range(N):
        row = random.randint(0, N-1)
        state['board'][row][col] = 'Q'

    return state


def showState(state):
    for row in state['board']:
        for col in row:
            print(col, end=' ')
        print()
    print()


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

    if qR == oR:
        return True

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

    while True:

        currentH = heuristic(current)

        if currentH == 0:
            return current

        neighbors = generateNeighbors(current)

        bestNeighbor = current
        bestH = currentH

        for n in neighbors:

            # Heuristic = Number of attacking queen pairs
            h = heuristic(n)

            if h < bestH:
                bestNeighbor = n
                bestH = h

        if bestH >= currentH:
            return None

        current = bestNeighbor


def main():

    solution = None

    while solution is None:
        solution = hillClimb()

    print("Solution Found!\n")
    showState(solution)


main()
