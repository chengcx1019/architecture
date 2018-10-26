if [ ! -d "deps" ]; then
  echo "Downloading zookeeper"
  wget http://apache.fayea.com/zookeeper/zookeeper-3.4.13/zookeeper-3.4.13.tar.gz  -P ./deps
else
  echo "Dependencies found, skipping retrieval..."
fi

docker build . -t zookeeperbase:latest