from pyspark import SparkConf, SparkContext
conf = SparkConf()
sc = SparkContext(conf=conf)

def multiplication(a, b):
    
    a = sc.textFile(a).map(lambda l: [float(i) for i in l.split(',')]).zipWithIndex().map(
        lambda l: (l[1], [(col, item) for col, item in enumerate(l[0])])).flatMapValues(
        lambda l: [i for i in l]).map(lambda l: (l[1][0], (l[0], l[1][1])))
    b = sc.textFile(b).map(lambda l: [float(i) for i in l.split(',')]).zipWithIndex().map(
        lambda l: (l[1], l[0])).flatMapValues(lambda l: [i for i in l])
    
    return a.join(b).map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1])).reduceByKey(lambda n1, n2: n1 + n2)


res = multiplication('a.txt', 'b.txt')

print(type(res))

print([i[1] for i in res.collect()])
