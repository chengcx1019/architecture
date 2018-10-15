# -*- coding: utf-8 -*-
import os
import sys

SPARK_HOME = '/home/hadoop'  + '/spark'


os.environ['SPARK_HOME'] = SPARK_HOME
sys.path.append(SPARK_HOME + "/python")
sys.path.append(SPARK_HOME + "/python/lib/py4j-0.10.7-src.zip")
print(sys.path)

from pyspark import SparkContext, SparkConf, Row

appName = "spark2django"  # 应用程序名称
master = "spark://localhost:8080"  # 222.28.78.90:7077为主节点ip和端口，请换成自己的主节点主机名称
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
def getTest():
    data = [1, 2, 3, 4, 5]
    distData = sc.parallelize(data)
    res = distData.reduce(lambda a, b: a + b)
    print (res)
    return res
def textfile():
    text_file = sc.textFile("hdfs:///sparkdir/dfile1")
    print(text_file.collect())
    df = text_file.map(lambda r: Row(r)).toDF(["line"])
    print(df)
if __name__ == '__main__':
    getTest()
    #textfile()
