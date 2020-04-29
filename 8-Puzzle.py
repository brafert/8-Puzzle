# Solving the 8-Puzzle Problem Using A*
from queue import PriorityQueue
import copy


class Node:
    # Node constructor
    def __init__(self, state):
        self.state = state      # state is current configuration of the puzzle
        self.children = []      # will hold legal moves according to the state

    # objects must be less-than comparable to add to priority queue
    def __lt__(self, other):
        if self.state[0][0] < other.state[0][0]:
            return True
        return False

    # Find child nodes from legal moves
    def find_children(self):
        y = -1      # row index of puzzle

        for row in self.state:     # y index
            y += 1
            x = -1
            for tile in row:       # x index
                x += 1
                if tile == '_':
                    moves = self.find_moves(x, y)
                    # Create children from possible moves
                    if "U" in moves:
                        new_state = copy.deepcopy(self.state)
                        child = Node(new_state)  # new child node

                        # swap space '_' with a tile
                        child.state[y][x] = child.state[y + 1][x]
                        child.state[y + 1][x] = "_"

                        self.children.append(child)  # add new child to list

                    if "D" in moves:
                        new_state = copy.deepcopy(self.state)
                        child = Node(new_state)  # new child node

                        # swap space '_' with a tile
                        child.state[y][x] = child.state[y - 1][x]
                        child.state[y - 1][x] = "_"

                        self.children.append(child)  # add new child to list

                    if "L" in moves:
                        new_state = copy.deepcopy(self.state)
                        child = Node(new_state)  # new child node

                        # swap space '_' with a tile
                        child.state[y][x] = child.state[y][x + 1]
                        child.state[y][x + 1] = "_"

                        self.children.append(child)  # add new child to list

                    if "R" in moves:
                        new_state = copy.deepcopy(self.state)
                        child = Node(new_state)  # new child node

                        # swap space '_' with a tile
                        child.state[y][x] = child.state[y][x - 1]
                        child.state[y][x - 1] = "_"

                        self.children.append(child)  # add new child to list

        return

    # Finds legal moves according to location of space '_'
    def find_moves(self, x, y):
        moves = ""

        # empty space is on top row
        if y == 0:
            moves += "U"    # can move a tile up

            if x == 0:
                moves += "L"    # can move a tile left
            if x == 1:
                moves += "LR"   # can move a tile left or right
            if x == 2:
                moves += "R"     # can move a tile right

        # middle row
        if y == 1:
            moves += "UD"   # can move a tile up or down

            if x == 0:
                moves += "L"    # can move a tile left
            if x == 1:
                moves += "LR"   # can move a tile left or right
            if x == 2:
                moves += "R"     # can move a tile right

        # bottom row
        if y == 2:
            moves += "D"  # can move a tile down

            if x == 0:
                moves += "L"  # can move a tile left
            if x == 1:
                moves += "LR"  # can move a tile left or right
            if x == 2:
                moves += "R"  # can move a tile right

        return moves


# Helper method for manhattan(), finds location of a tile in the goal state
def find_index(tile, goal):
    for y, row in enumerate(goal):  # y index
        for x, goalTile in enumerate(row):    # x index
            if tile == goalTile:
                return y, x


# Heuristic function, calculates the sum of Manhattan distances for each tile
def manhattan(state, goal):
    total = 0

    for state_y, row in enumerate(state):  # y index
        for state_x, tile in enumerate(row):    # x index
            goal_y, goal_x = find_index(tile, goal)
            dx = abs(state_x - goal_x)
            dy = abs(state_y - goal_y)
            total += dx + dy

    return total


# Heuristic function, calculates number of tiles that aren't in their final position in the goal state
def hamming(state, goal):
    total = 0       # Hamming distance

    for y, row in enumerate(state):  # y index
        for x, tile in enumerate(row):  # x index
            if tile != goal[y][x]:
                total += 1

    return total


# Prints the moves made to solve the puzzle
def print_puzzle(endNode, parents, cost):
    print(f"Goal reached after: {cost} moves.")

    moves = []
    moves.append(endNode)    # final move (reached the goal state)

    # Find all ancestors of the endNode to get the moves
    parent = parents[endNode]
    while parent != None:
        moves.append(parent)
        parent = parents[parent]

    # Print the moves from start state to goal state
    moves.reverse()
    for move in moves:
        print(move.state)
        print()

    return


# Runs the A* algorithm to solve the 8-Puzzle
def solve(start, goal, heuristic):
    print("Beginning A* Search. Please wait, this may take a moment...\n")

    open = PriorityQueue()      # nodes to visit

    startState = Node(start)    # starting node
    goalState = Node(goal)      # goal node

    open.put((0, startState))    # add start position to nodes to visit

    # Dictionaries to hold parents and costs of nodes
    parent = {}         # came_from
    pathCost = {}       # cost_so_far

    # starting node has no parent or cost
    parent[startState] = None
    pathCost[startState] = 0

    while not open.empty():
        lowest = open.get()
        current = lowest[1]

        current.find_children()

        # print(pathCost[current])

        if current.state == goalState.state:
            print_puzzle(current, parent, pathCost[current])
            break

        for child in current.children:
            childCost = pathCost[current] + 1       # new cost equal to current cost + 1 for moving a tile

            # child has not been visited or is cheaper than current path
            if child not in pathCost or childCost < pathCost[child]:

                pathCost[child] = childCost

                priority = 0
                if heuristic == '1':    # Manhattan distance
                    priority = (childCost + manhattan(child.state, goal))
                if heuristic == '2':    # Hamming distance
                    priority = (childCost + hamming(child.state, goal))

                open.put((priority, child))     # add child node to list of nodes to visit with priority of f(child)
                parent[child] = current

    return


# Uses user input to create puzzle board
def set_state():
    puzzle = []
    for i in range(0, 3):
        line = input().split()
        puzzle.append(line)
    return puzzle


def main():
    # create start and goal states
    print("Enter start state: ")
    start = set_state()
    print(f"You entered: {start}")
    print("Enter goal state: ")
    goal = set_state()
    print(f"You entered: {goal}")

    print("Select a heuristic function. \nEnter '1' for Manhattan distance or '2' for Hamming distance.")
    heuristic = input()

    # solve puzzle
    solve(start, goal, heuristic)


if __name__ == "__main__":
    main()
