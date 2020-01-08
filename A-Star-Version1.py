class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, goal, energy):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list, closed_list = [], []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0 and energy > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        # enumerate: loop over somthing and have a automatic counter for counter, value in enumerate(list)
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1),
                             (1, 1)]:  # Adjacent squares(around parent)

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue
            ''' add walls '''
            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def setMazecontent(maze, positions, itemValue):
    for index, col in positions.iterrows():
        x, y = col
        maze[x][y] = itemValue
    return maze


def setWalls(maze, positions):
    for index, col in positions.iterrows():
        x1, y1, x2, y2 = col
        maze[x1][y1] = 8
        maze[x2][y2] = 9
    return maze


def getMaze():
    import pandas as pd
    import numpy as np

    # Generate Empty maze
    maze = np.zeros((10, 10))
    print('### 1) Generate Clean Maze ###')
    print(maze)

    # set Walls
    print('### 2) Get Wall data from csv ###')
    try:
        wallFile = input()
    except:
        wallFile = 'CSV-Data/S_A01_Mauer.csv'
    position_walls = pd.read_csv(wallFile, sep=';', header=None)
    position_walls.values
    print('### 3) Set Wall Data in maze ###')
    # maze = setWalls(maze, position_walls)
    # print(maze)

    # set Stars (2)
    print('### 4) Get Star data from csv ###')
    try:
        starFile = input()
    except:
        starFile = 'CSV-Data/S_A01_Stern.csv'
    position_stars = pd.read_csv(starFile, sep=';', header=None)
    position_stars.values
    print('### 5) Set Star Data in maze ###')
    # maze = setMazecontent(maze, position_stars, 2)
    # print(maze)

    # Set energy (3)
    print('### 6) Get Energy data from csv ###')
    try:
        energyFile = input()
    except:
        energyFile = 'CSV-Data/S_A01_Energie.csv'
    position_energy = pd.read_csv(energyFile, sep=';', header=None)
    position_energy.values
    print('### 7) Set Star Data in maze ###')
    # maze = setMazecontent(maze, position_energy, 3)
    '''
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    #print(maze)
    '''

    '''
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    return maze


def main(start, goal, energy):
    path = astar(getMaze(), start, goal, energy)
    print('### 8) Print Path ###')
    print(path)


if __name__ == '__main__':
    # Input start coordinate in format x,y if left empty will default to 0,0
    print("### Enter start as: x,y | default 0, 0")
    try:
        start = input()
        sx, sy = start.split(",", 2)
        sx, sy = int(sx), int(sy)
    except:
        sx = 0
        sy = 0

    # Input goal coordinate in format x,y if left empty will default to  9, 9
    print("### Enter goal as: x,y | default 9, 9")
    try:
        goal = input()
        gx, gy = goal.split(",", 2)
        gx, gy = int(gx), int(gy)
    except:
        gx = 9
        gy = 9

    # Input energy as number if left empty will default to 5
    print("### Enter energy as number default 5")
    try:
        e = input()
        e = int(e)
    except:
        e = 5
    print("start:(" + str(sx) + "," + str(sy) + ") goal:(" + str(gx) + "," + str(gy) + ") energy:(" + str(e) + ")")

    main((sx, sy), (gx, gy), e)