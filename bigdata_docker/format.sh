#!/usr/bin/env bash
docker exec -it --user hadoop hadoop-master /home/hadoop/hadoop/sbin/stop-dfs.sh
docker exec -it --user hadoop hadoop-master /home/hadoop/hadoop/sbin/stop-yarn.sh
docker exec -it hadoop-master rm -r  /data/dataNode/current/
docker exec -it hadoop-slave1 rm -r  /data/dataNode/current/
docker exec -it hadoop-slave2 rm -r  /data/dataNode/current/
docker exec -it hadoop-slave3 rm -r  /data/dataNode/current/
docker exec -it --user hadoop hadoop-master hdfs namenode -format
docker exec -it --user hadoop hadoop-master /home/hadoop/hadoop/sbin/start-dfs.sh
docker exec -it --user hadoop hadoop-master /home/hadoop/hadoop/sbin/start-yarn.sh
docker exec -it --user hadoop hadoop-master jps
docker exec -it --user hadoop hadoop-slave1 jps