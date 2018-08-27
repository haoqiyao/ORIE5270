def get_structure(name_txt_file):
    
    #initialize the dict
    bellman_final = {}
    bellman_single = {}
    
    #parse the txt file
    bellman = open(name_txt_file, "r").read().split()
    adj = {}
    costs = {}
    for i in range(len(bellman)):
        if i % 2 == 0:
            adj_array = []
            if eval(bellman[i + 1])!=None:
                for j in range(1, len(bellman[i + 1]), 6):
                    adj_array.append(eval(bellman[i + 1][j]))
                    if bellman[i + 1][j + 2] == "-":
                        costs[(int(bellman[i]), eval(bellman[i + 1][j]))] = int(bellman[i + 1][j + 2:j + 4])
                    else:
                        costs[(int(bellman[i]), eval(bellman[i + 1][j]))] = int(bellman[i + 1][j + 2])
                adj[int(bellman[i])] = adj_array
            else:
                bellman_final[i] = {}    

    keys = set()
    for i in range(len(costs.keys())):
        keys.add(costs.keys()[i][0])

    for key in keys:

        for source, destination in costs.keys():  
            if source == key:
                bellman_single[destination] = costs[source, destination]

        bellman_final[key] = bellman_single
        bellman_single = {}
        
    return bellman_final






def find_negative_circles(dictionary, source):
    
    #start from newly added node 0
    source_node = {}
    for i in range(1, len(dictionary)+1):
        source_node[i] = 0
    dictionary[0] = source_node
    
    #initialize two dict, minimal distance and previous node
    dist = {}
    prev = {}
    
    #initialize all vertices as minimal distance is infinite and previous node is None
    for all_v in dictionary:
        prev[all_v] = None
        dist[all_v] = float('Inf')
    
    #start from source, source's dist is 0
    dist[source] = 0
    
    #run through the map with N-1 times, with N equals to the number of vertices
    for i in range(len(dictionary)-1):
        
        #go through all the vertices
        for curr_v in dictionary:
            
            #same as Dijkstra, if find a shorter path, update the dist dict
            for adj_v in dictionary[curr_v]:
                if dist[adj_v] > dist[curr_v] + dictionary[curr_v][adj_v]:
                    dist[adj_v] = dist[curr_v] + dictionary[curr_v][adj_v]
                    prev[adj_v] = curr_v
    
    #add a flag to check whether the map has negative cycle. If it has, the #N loop can still decrease the weight
    negative_cycle_flag = False
    
    #check if the #N can still decrease the cost
    for curr_v in dictionary:
        for adj_v in dictionary[curr_v]:
            if dist[adj_v] > dist[curr_v] + dictionary[curr_v][adj_v]:
                negative_cycle_flag = True
                
                #if find a negative cycle, trace back to the problem node and make the cycle path
                start = curr_v
                path = [start]
                while prev[start] != curr_v:
                    path.append(prev[start])
                    start = prev[start]
    
    return negative_cycle_flag, path

dictionary = get_structure("bellman.txt")
source = 0
negative_cycle_flag, path = find_negative_circles(dictionary, source)

print("Does the map have negative cycle? " + str(negative_cycle_flag))
print("The negative cycle path is: " + str(path))
