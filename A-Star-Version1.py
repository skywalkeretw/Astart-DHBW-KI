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

class InputData():
    def __init__(self):
        self.walls = None
        self.energy = None
        self.stars = None
        self.start = None
        self.goal = None
        self.startEnergy = None
        self.maze = None


    def clear(self):
        self.walls = None
        self.energy = None
        self.stars = None
        self.start = None
        self.goal = None
        self.startEnergy = None
        self.maze = None

inputData = InputData()


def astar(maze, start, goal, energy):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0
    stars = 0
    # Initialize both open and closed list
    open_list, closed_list = [], []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0 and energy > 0:

        # Get the current node
        current_node, current_index = open_list[0], 0

        # enumerate: loop over somthing and have a automatic counter for counter, value in enumerate(list)
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        if maze[current_node.position[0]][current_node.position[1]] == 2 or maze[current_node.position[0]][current_node.position[1]] == 3:
            energy += 5
            maze[current_node.position[0]][current_node.position[1]] -= 2

        if maze[current_node.position[0]][current_node.position[1]] == 4 or maze[current_node.position[0]][current_node.position[1]] == 5:
            stars += 2
            maze[current_node.position[0]][current_node.position[1]] -= 4
        # decrease energy by one
        energy -= 1

        # Found the goal
        if current_node == end_node:
            return returnAstar(current_node, energy, stars, True)

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares(around parent)
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            #Empty Field
            if maze[node_position[0]][node_position[1]] == 0:
                children = appendChildNode(children, current_node, node_position)

            # Wall between filds
            if maze[current_node.position[0]][current_node.position[1]] == 1 and maze[node_position[0]][node_position[1]] == 1 \
                or maze[current_node.position[0]][current_node.position[1]] == 1 and maze[node_position[0]][node_position[1]] == 3 \
                or maze[current_node.position[0]][current_node.position[1]] == 1 and maze[node_position[0]][node_position[1]] == 5:
                continue



            # Energy is on field
            if maze[node_position[0]][node_position[1]] == 2:
                children = appendChildNode(children, current_node, node_position)

            # Star is on field
            if maze[node_position[0]][node_position[1]] == 4:
                children = appendChildNode(children, current_node, node_position)


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
        #print(open_list)
    return returnAstar(open_list[0], energy, stars, False)

def returnAstar(current_node, energy, stars, fin):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1], energy, stars, fin # Return reversed path

def appendChildNode(children, current_node, node_position):
    # Create new node
    new_node = Node(current_node, node_position)
    # Append
    children.append(new_node)
    return children

def setMazecontent(maze, positions, itemValue):
    for index in range(0,len(positions)):
        x, y = positions[index]
        if maze[x][y] == 0 or maze[x][y] == 1:
            maze[x][y] += itemValue
    return maze

def setWalls(maze, positions):
    for index in range(0,len(positions)):
        x1, y1, x2, y2 = positions[index]
        maze[x1][y1] = maze[x2][y2] = 1
    return maze

def getFileName(name):
    from tkinter import filedialog
    if name == 'walls':
        inputData.walls = filedialog.askopenfilename()
    if name == 'stars':
        inputData.stars = filedialog.askopenfilename()
    if name == 'energy':
        inputData.energy = filedialog.askopenfilename()

def guiStart():
    import tkinter as tk
    root = tk.Tk()

    startLable = tk.Label(root, text="Start value")
    startLable.pack()
    startEntry = tk.Entry(root, width=50)
    startEntry.pack()
    startEntry.insert(0, "0,0")
    inputData.start = startEndPosition(startEntry.get())

    goalLable = tk.Label(root, text="Goal value")
    goalLable.pack()
    goalEntry = tk.Entry(root, width=50)
    goalEntry.pack()
    goalEntry.insert(0, "9,9")
    inputData.goal = startEndPosition(goalEntry.get())

    startEnergyLable = tk.Label(root, text="Goal value")
    startEnergyLable.pack()
    startEnergyEntry = tk.Entry(root, width=50)
    startEnergyEntry.pack()
    startEnergyEntry.insert(0, "15")
    inputData.startEnergy = int(startEnergyEntry.get())

    getWallsBtn = tk.Button(root, text="Get Walls", command=lambda: getFileName('walls'))
    getWallsBtn.pack()
    #wallFileLable = tk.Label(root, text=inputData.walls)
    #wallFileLable.pack()

    getEnergysBtn = tk.Button(root, text="Get Energy", command=lambda: getFileName('stars'))
    getEnergysBtn.pack()
    #energyFileLable = tk.Label(root, text=inputData.walls)
    #energyFileLable.pack()

    getStarsBtn = tk.Button(root, text="Get Stars", command=lambda: getFileName('energy'))
    getStarsBtn.pack()
    #starFileLable = tk.Label(root, text=inputData.walls)
    #starFileLable.pack()


    goBtn = tk.Button(root, text="Run", command=lambda: displayGuiAStar(root,tk))
    goBtn.pack()

    root.mainloop()



def displayGuiAStar(root, tk):
    import numpy as np
    maze = np.zeros((10, 10))
    maze = setWalls(maze, itemPosition(inputData.walls))
    maze = setMazecontent(maze, itemPosition(inputData.energy), 2)
    maze = setMazecontent(maze, itemPosition(inputData.stars), 4)
    path, endEnergy, stars, completed = astar(maze, inputData.start, inputData.goal, inputData.startEnergy)
    out = "Path: " +str(path).strip('[').strip(']').replace(',', ' ->') + "\nStars: " + str(stars) + "\nEnergy left: " + str(endEnergy)
    output = tk.Label(root, text=out)
    output.pack()
    pass
def cmdStart(args):
    # Input start coordinate in format x,y if left empty will default to 0,0
    print("### Enter start as: x,y | default 0, 0")
    start = startEndPosition(args.start)

    # Input goal coordinate in format x,y if left empty will default to  9, 9
    print("### Enter goal as: x,y | default 9, 9")
    goal = startEndPosition(args.goal)

    # Input energy as number if left empty will default to 5
    print("### Enter energy as number default 5")
    try:
        e = args.startenergy
        e = int(e)
    except:
        e = 20

    start, goal, startEnergy = start, goal, e
    print(startEnergy)
    import numpy as np
    # Generate Empty maze
    maze = np.zeros((10, 10))
    print('### 1) Generate Clean Maze ###')
    print(maze)

    # set Walls
    print('### 2) Get Wall data from csv if empty uses example csv ###')
    wallFile = args.walls
    fileExists(wallFile)
    print('### 3) Set Wall Data in maze ###')
    maze = setWalls(maze, itemPosition(wallFile))
    # print(maze)

    # Set energy (2 or 3)
    print('### 4) Get Energy data from csv if empty uses example csv###')
    energyFile = args.energy
    fileExists(energyFile)
    print('### 5) Set Star Data in maze ###')
    maze = setMazecontent(maze, itemPosition(energyFile), 2)

    # set Stars (4 or 5)
    print('### 6) Get Star data from csv if empty uses example csv###')
    starFile = args.stars
    print('### 7) Set Star Data in maze ###')
    maze = setMazecontent(maze, itemPosition(starFile), 4)

    path, endEnergy, stars, completed = astar(maze, start, goal, startEnergy)

    if completed:
        print('### 8) A* was successful ###')
    else:
        print('### 8) Not enough energy to Finish displaying information as far as we got ###')
    print('### 9) Print Path ###')
    print(path)
    print("### 10) Print energy ###")
    print(endEnergy)
    print('### 11) print stars ###')
    print(stars)


def startEndPosition(args):
    try:
        x, y = args.split(",", 2)
        x, y = int(x), int(y)
    except:
        x, y = 0, 0
    return (x, y)


def itemPosition(file):
    import pandas as pd
    position_stars = pd.read_csv(file, sep=';', header=None)
    return position_stars.values


def fileExists(file):
    import sys
    from os import path
    if not path.exists(file):
        print('File:' + file + ' doesnt exist')
        sys.exit()


if __name__ == '__main__':
    import argparse as argp
    parser = argp.ArgumentParser()
    parser.add_argument('-s', '--start', help='Startvalue as: "x,y"')
    parser.add_argument('-g', '--goal', help='Goalvalue as: "x,y"')
    parser.add_argument('-se', '--startenergy', help='Energy as number')
    parser.add_argument('-w', '--walls', help='Path to wall csv')
    parser.add_argument('-st', '--stars', help='Path to star csv')
    parser.add_argument('-e', '--energy', help='Path to energy csv')
    args = parser.parse_args()

    if (args.energy is not None
            and args.goal is not None
            and args.stars is not None
            and args.start is not None
            and args.startenergy is not None
            and args.energy is not None
            and args.walls):
        print("Start CMD")
        cmdStart(args)
    else:
        guiStart()
