import sys
import math
import re
import numpy as np


def findDistance(x1, x2,y1,y2):
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return int(round(distance))

def findMin(firstLine, key, trees):
    minimum = 999999
    min_num =0
    for sure in range(firstLine):
        if key[sure]<minimum and trees[sure] == False:
            minimum = key[sure]
            min_num = sure
    return min_num

def prims(firstLine, distance):
    #value to get minimum weight
    key = [999999] * firstLine
    #array to store the spannning tree
    y = [0] * firstLine
    #make sure to pick the first vertex
    key[0]=0
    trees = [False] * firstLine
    #get the first node
    y[0] = -1

    for num in range(firstLine):
        get = findMin(firstLine, key, trees)
        trees[get] = True
        for v in range(firstLine):
            if distance[get][v] > 0 and trees[v] == False and key[v] > distance[get][v]:
                key[v] = distance[get][v]
                y[v] = get
    #findWeight(firstLine, y, distance)   
    
    return y

def adgency_matrix(y):
    matrix =np.zeros((len(y), len(y)))
    #if len(y) < 5: print matrix

    for node in range(len(y)):
        for other in range(node+1, len(y)):
            if y[node] == other or y[other] == node:
                matrix[node][other] = 1
                matrix[other][node] = 1
    return(matrix)

def outputFile(visited, total_distance):
    fileName = str(sys.argv[1])
    f = open(fileName + ".tour", "w")
    f.write(str(total_distance))
    for i in range(len(visited)):
        f.write("\n")
        f.write(str(visited[i]))
    f.close

def dfsvisit(matrix, visited, u):
    visited.append(u)
    for visit in range(0, len(matrix[u])):
        if matrix[u][visit] == 1 and visit not in visited:
            dfsvisit(matrix, visited, visit)
    return visited

def dfs(matrix, distance):
    visited = []
    visited = dfsvisit(matrix, visited, 0)
    total_distance = 0

    for v in range(0, len(visited)-1):
        total_distance += distance[visited[v]][visited[v+1]]
    total_distance += distance[visited[len(visited)-1]][visited[0]]
    outputFile(visited, total_distance)

def main():
    #reading from the input files
 #.strip to cut off white space   
    
    with open(sys.argv[1], 'r') as fileName:
        graph_nodes = []
        firstLine = int(fileName.readline())
        #print(firstLine)
        for line in range(firstLine):
            nodes = fileName.readline().strip()
            [c, x, y] = [int(j) for j in nodes.split()]
            graph_nodes.append([c, x, y])
        distance = []
        i = 0
        #creating and assigning all of the nodes
        for i in range(int(firstLine)):
            temp = []
            j = i+1
            for j in range(int(firstLine)):
                x1 = graph_nodes[i][1]
                x2 = graph_nodes[j][1]
                y1 = graph_nodes[i][2]
                y2 = graph_nodes[j][2]
                temp.append(findDistance(x1,x2,y1,y2))
            distance.append(temp)
            #print(distance)
    y = [0] * firstLine
    mat = adgency_matrix(y)
    answer = dfs(mat, distance)
            
            
        
if __name__ == "__main__":
    main()          
        






"""
Function to calculate the distnace between nodes
"""
"""
Function to find minimum node based on the save adgency matrix
"""
"""
Function to find the minimum distance
"""
"""
Function to calculate the weight
"""
"""
Main function to open the file and apppend all of the values
"""
