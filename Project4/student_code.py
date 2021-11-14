import math

def shortest_path(M,start,goal):
    print("shortest path called")
    explored = {}
    frontier = {start:(0, get_euclidean_distance(M, start, goal), [start])} # g, h, path
    
    while frontier:
        properties_list = [[key, val[0], val[1], val[2]] for key, val in sorted(frontier.items(), key=lambda x:x[1][0]+x[1][1])]
        curr_node, curr_g, curr_h, curr_path = properties_list[0]
        if curr_node == goal:
            break
            
        explored[curr_node] = frontier.pop(curr_node)
        
        for next_node in M.roads[curr_node]:
            next_path = curr_path.copy()
            next_path.append(next_node)
            next_g = curr_g + get_euclidean_distance(M, curr_node, next_node)
            
            if next_node not in explored:
                if next_node not in frontier:
                    frontier[next_node] = [next_g, get_euclidean_distance(M, next_node, goal), next_path]
                else:
                    if next_g < frontier[next_node][0]:
                        frontier[next_node][0], frontier[next_node][2] = next_g, next_path
                
    return frontier[goal][2]


def get_euclidean_distance(M, nodeA, nodeB):
    '''Euclidean Distance refers to the length of a straight line between the two points.
    In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is the square root of (x1 - x2)^2 + (y1 - y2)^2.
    It is used to calculate the actual distance when you are allowed to move straight from one point to another.'''
    return math.sqrt(sum((a-b)**2 for a, b in zip(M.intersections[nodeA], M.intersections[nodeB])))

def get_diagonal_distance(M, nodeA, nodeB):
    '''Diagonal Distance refers to the distance of the two points, made by only three directions allowed - 
    horizontal, vertical, and diagonally. It is used when you are allowed to move those three directions.
    (Imagine yourself as a King in chess. You are allowed to move either horizontally, vertically, or diagonally.)'''
    aX, aY = M.intersections[nodeA]
    bX, bY = M.intersections[nodeB]
    
    dx = abs(aX - bX)
    dy = abs(aY - bY)

    return dx + dy + (math.sqrt(2) - 2)*min(dx, dy)

def get_manhattan_distance(M, nodeA, nodeB):
    '''Manhattan Distance refers to the distance of the two points, made by only two directions allowed - 
    horizontal and vertial. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.
    (Image yourself as a person in Manhattan, trying to calculate the actual walk-distance from Empire State Building
    to World Trade Center. You are allowed to move either horizontally or vertically.)'''
    return sum(abs(a-b) for a, b in zip(M.intersections[nodeA], M.intersections[nodeB]))
    
    
  