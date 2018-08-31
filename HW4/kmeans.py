import numpy as np
from pyspark import SparkConf, SparkContext

#open the package machine
conf = SparkConf()
sc = SparkContext(conf=conf)

def kmeans(Data, Centroid, iterations):

    #read the data and the centroid
    data = sc.textFile(Data).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()
    
    centroid = sc.textFile(Centroid).map(lambda line: np.array([float(x) for x in line.split(' ')])).collect()

    
    #run 100 times. 
    for i in range(iterations):

        #previous centroid
        centroid_prev = centroid
        
        #use update centroid function to map each  point to centroid
        match = data.map(lambda x: (update_centroid(x, centroid_prev), x))
        
        #sum all the numbers based on the centroid assigned
        sum_cent = match.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
        
        #update the centroid using average value
        centroid_curr = sum_cent.map(lambda x: x[1][0] / x[1][1]).collect()

    
    #write the centroid data into the txt file
    f = open("kmeans_result.txt", "w")
    
    for cent in centroid_curr:
        
        l = ""
        
        for x in cent:
            
            l += str(x) + " "
            
        f.write(l + "\n")
        
    f.close()
    
    
#update centroid function
def update_centroid(example, centroid_array):

    min_dist = 10000000
    
    new_centroid = 0
    
    for cent_loc, cent in enumerate(centroid_array):
        
        #new distance
        dist = np.linalg.norm(example - cent)
        
        #if smaller than the min, update it and change the centroid index
        if dist < min_dist:
            
            min_dist = dist
            
            new_centroid = cent_loc
            
    return new_centroid


iterations = 100
kmeans('data.txt', 'c1.txt', iterations)
