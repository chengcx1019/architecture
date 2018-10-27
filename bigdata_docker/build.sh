#!/usr/bin/env bash
docker network create --subnet=202.204.60.240/28 zoo
cd scalabase && ./build.sh && cd -
cd zookeeperbase && ./build.sh && cd -
docker-compose -f docker-compose-zk.yml up -d
docker-compose -f docker-compose-mysql.yml up -d
cd hadoopbase && ./build.sh && cd -
cd hivebase && ./build.sh && cd -
cd sparkbase && ./build.sh && cd -
cd hbasebase && ./build.sh && cd -
docker-compose -f docker-compose-hbase.yml up -d
cd dataxbase && ./build.sh && cd -
docker-compose -f docker-compose-datax.yml up -d

