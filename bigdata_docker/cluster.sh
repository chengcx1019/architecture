#!/bin/bash

# Bring the services up
function build {
    echo ">> build all ..."
    cd scalabase && ./build.sh && cd -
    sleep 5
    cd zookeeperbase && ./build.sh && cd -
    sleep 5
    cd hadoopbase && ./build.sh && cd -
    sleep 5
    cd hivebase && ./build.sh && cd -
    sleep 5
    cd sparkbase && ./build.sh && cd -
    sleep 5
    cd hbasebase && ./build.sh && cd -
    sleep 5
    cd dataxbase && ./build.sh && cd -
    sleep 5
}

if [[ $1 = "build" ]]; then
    build
    exit
fi

if [[ $1 = "start" ]]; then
    echo ">> create subnet zoo ..."
    docker network rm zoo
    docker network create --subnet=202.204.60.240/28 zoo # create custom network
    echo ">> start zookeeper ..."
    docker-compose -f docker-compose-zk.yml up -d
    echo ">> start mysql ..."
    docker-compose -f docker-compose-mysql.yml up -d
    echo ">> start hadoop,hive,spark,hbase ..."
    docker-compose -f docker-compose-hbase.yml up -d
    echo ">> start datax ..."
    docker-compose -f docker-compose-datax.yml up -d
  exit
fi

if [[ $1 = "stop" ]]; then
  echo ">> Stop hadoop ..."
    docker exec -u hadoop -it hadoop-master hadoop/sbin/stop-all.sh
    echo ">> Stop spark ..."
    docker exec -u hadoop -it hadoop-master spark/sbin/stop-all.sh
    echo ">> Ensure status ..."
    docker exec -u hadoop -it hadoop-master jps
  exit
fi

if [[ $1 = "deploy" ]]; then
    #  docker rm -f `docker ps -aq` # delete old containers
    # Format nodemaster
    echo ">> Formatting hdfs ..."
    docker exec -u hadoop -it hadoop-master hadoop/bin/hdfs namenode -format
    sleep 5
    echo ">> Start hadoop ..."
    docker exec -u hadoop -it hadoop-master hadoop/sbin/start-dfs.sh
    sleep 5
    docker exec -u hadoop -it hadoop-master hadoop/sbin/start-yarn.sh
    sleep 5
    echo ">> Start spark ..."
    docker exec -u hadoop -it hadoop-master spark/sbin/start-all.sh
    sleep 5
    echo ">> Ensure status ..."
    docker exec -u hadoop -it hadoop-master jps
    echo "Hadoop info @ hadoop-master: http://localhost:8088/cluster"
    echo "Spark info @ hadoop-master  : http://localhost:8080/"
    exit
fi

echo "Usage: cluster.sh deploy|start|stop"
echo "                 deploy - start hadoop and spark service"
echo "                 build   - build all images"
echo "                 create  - create the start containers"
echo "                 stop   - stop the running containers"