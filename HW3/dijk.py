import heapq as hq

def find_shortest_path(name_txt_file, source, destination):
    
    
    #parse the txt file to make the data usable
    dijk = open(name_txt_file, "r").read().split()
    adj = {}
    costs = {}
    for i in range(len(dijk)):
        if i % 2 == 0:
            adj_array = []
            for j in range(1, len(dijk[i + 1]), 6):
                adj_array.append(eval(dijk[i + 1][j]))
                costs[(int(dijk[i]), eval(dijk[i + 1][j]))] = int(dijk[i + 1][j + 2])
            adj[int(dijk[i])] = adj_array  
      
    #make the costs dict with two-way weight
    two_way_cost = {}
    for key, weight in costs.iteritems():
        two_way_cost[key] = weight
        two_way_cost[(key[1],key[0])] = weight
    costs = two_way_cost
    
    
    #The dict of the minimal distance with the structure: {vertex: cost of the source to vertex}
    dist = {}
    
    #The dict of many info with the structure: {vertex: [distance of source to vertex, parent of the vertex, vertex]}
    info = {}
    
    #The priority queue
    p_q = []
    
    #The dict to keep track of the previous vertices
    prev = {}
    
    #Settled set that keep the visited vertices
    settled = set()
    
    #Start with source
    dist[source] = 0
    settled.add(source)
    
    
    
    #Using the adjacency dict to get all the adjacent vertices of source
    for adj_v in adj.get(source, []):
        
        #Put the original cost into the minimal distance dict. Will change afterwards
        dist[adj_v] = costs[source, adj_v]
        
        temp_path = [dist[adj_v], source, adj_v]
        
        #Append the same array into the info dict
        info[adj_v] = temp_path
        
        #Using heap to append the priority queue
        hq.heappush(p_q, temp_path)
    
    while p_q:
        
        #if the priority queue not empty, pop the first element in the queue
        distance, previous, temp_v = hq.heappop(p_q)
        
        #if the adjacent vertex not visited
        if (temp_v in settled) == 0:
            
            #append prev dict with the source vertex as the adjacent vertex's parent
            prev[temp_v] = previous
            
            #add adjacent vertex into the settled set
            settled.add(temp_v)
            
            #if adjacent vertex is already the end, output the prev dict and the dist dict
            if temp_v == destination:
                return prev, dist[temp_v]
            
            #else, for the vertex that are adjacent to the adjacent vertex (double adjacent vertex)
            for adj_adj_v in adj.get(temp_v, []):
                
                #if the dist dict has the double adjacent vertex, which means the source can access the 
                #double adjacent vertex directly
                if dist.get(adj_adj_v) == None:
                    
                    #if source cannot access the double adjacent vertex directly, add the dist with the summation
                    dist[adj_adj_v] = costs[temp_v, adj_adj_v] + dist[temp_v]
                    
                    temp_path = [dist[adj_adj_v], temp_v, adj_adj_v]
                    
                    #update info accordingly
                    info[adj_adj_v] = temp_path
                    
                    #push the priority queue with adjacent vertex as the new starting point
                    hq.heappush(p_q, temp_path)
                    
                else:
                    
                    #if the dist dict has the double adjacent vertex, which means the source can access the 
                    #double adjacent vertex directly
                    
                    #and if the distance of source to double adjacent vertex is larger than source to adjacent
                    #vertex + adjacent vertex to double adjacent vertex
                    if dist[adj_adj_v] > costs[temp_v, adj_adj_v] + dist[temp_v]:
                        
                        #change the minimal distance to the source to adjacent vertex + adjacent vertex to 
                        #double adjacent vertex
                        dist[adj_adj_v] = costs[temp_v, adj_adj_v] + dist[temp_v]
                        
                        #change the old parent vertex of the double adjacent vertex (source) into adjacent vertex
                        info[adj_adj_v][1] = temp_v
                        
                        #change the minimal dist of the double adjacent vertex into the new summation one
                        info[adj_adj_v][0] = dist[adj_adj_v]
                        
                        #previos start
                        temp_start = 0
                        
                        #new node position for double adjacent vertex
                        temp_index = p_q.index(info[adj_adj_v])
                        
                        #change the low priority with high priority since we change the shortest path of the 
                        #double adjacent vertex
                        hq._siftdown(p_q, temp_start, temp_index)
                    
                    

    return shortest_path, minimal_cost
    
    

source, destination = 1, 5

shortest_path, minimal_cost = find_shortest_path("dijk.txt", source, destination)


#get the shortest path
path = [destination]
dest_temp = destination
while dest_temp in shortest_path:
    path.append(shortest_path[dest_temp])
    dest_temp = shortest_path[dest_temp]
path = path[::-1]

print ("shortest_path from " + str(source) + " to " + str(destination) + " is " + str(path))
print ("The cost is " + str(minimal_cost))

print("The answer is " + str((minimal_cost, path)))
