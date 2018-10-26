if [ ! -d "deps" ]; then
  echo "Downloading hive"
  wget http://mirror.bit.edu.cn/apache/hive/hive-3.1.0/apache-hive-3.1.0-bin.tar.gz -P ./deps
  wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.39.tar.gz -P ./deps
else
  echo "Dependencies found, skipping retrieval..."
fi

docker build . -t hivebase:latest