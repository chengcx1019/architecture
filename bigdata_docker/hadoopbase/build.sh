if [ ! -d "deps" ]; then
  echo "Downloading hadoop"
  wget https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz -P ./deps
else
  echo "Dependencies found, skipping retrieval..."
fi

docker build . -t hadoopbase:latest