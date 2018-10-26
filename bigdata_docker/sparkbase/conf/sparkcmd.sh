#!/bin/bash

export USER=hadoop
source ~/.profile
if [[ $1 = "start" ]]; then
  if [[ $HOSTNAME = "hadoop-master" ]]; then
     ~/hadoop/sbin/start-dfs.sh
     ~/hadoop/sbin/start-yarn.sh
     ~/spark/sbin/start-master.sh
     exit
  fi
  ~/spark/sbin/start-slave.sh hadoop-master:7077
  exit
fi

if [[ $1 = "stop" ]]; then
  if [[ $HOSTNAME = "hadoop-master" ]]; then
     ~/hadoop/sbin/stop-dfs.sh
     ~/hadoop/sbin/stop-yarn.sh
     ~/spark/sbin/stop-master.sh
     exit
  fi
  ~/spark/sbin/stop-slave.sh
fi
