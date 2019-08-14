from math import sqrt
from queue import PriorityQueue


def shortest_path(M, start, goal):
    
    # A priority queue ensures removal of min node in O(1) time
    frontier_queue = PriorityQueue()
        
    # To trace back a path
    prev_link = {start: None}
    
    # path cost (g)
    G = {start: 0}
    
    ## Distance to the goal from each node i.e. h
    H = {}
    for node, coord in M.intersections.items():
        H[node] = calc_dist(M, node, goal)
        
        
    # Initialize a queue with start with its f value = g + h = 0 + h
    frontier_queue.put(start, H[start])
    
    
    # main loop
    while not frontier_queue.empty():
        
        # get a node from queue with min f value
        current_node = frontier_queue.get()
        
        if current_node == goal:
            reconstruct_path(prev_link, start, goal)
        
        # Get all frontiers of current-node
        for neighbor in M.roads[current_node]:
            
            # g_tentative is the path cost of neighbor from start through current_node
            g_tentative = G[current_node] + calc_dist(M, current_node, neighbor)
            
            # Proceed only if neighbor is not explored or its explored then 
            # g_tentative value should be less than G[neighbor]
            if neighbor not in G or g_tentative < G[neighbor]:
                G[neighbor] = g_tentative
                
                # f = g + h 
                f = g_tentative + H[neighbor]
                
                # add it to frontier_node 
                frontier_queue.put(neighbor, f)
                
                # link all neighbors to current_node (i.e. prev_node)
                prev_link[neighbor] = current_node
                #print(prev_link)
                
    return reconstruct_path(prev_link, start, goal) 
 

# Calculate distance (d)
def calc_dist(M, node1, node2):
    
    x1, y1 = tuple(M.intersections[node1])
    x2, y2 = tuple(M.intersections[node2])
    
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

# reconstruct path from prev link ones
def reconstruct_path(prev_link, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev_link.get(curr, None)
        # If start and goal are not connected, there will be a node
        # previous to goal that will have None value. 
        if curr == None:
            print("No path between start and goal!")
            return None
        path.append(curr)
        
    path.reverse()
    return path



    
    
    
    
    