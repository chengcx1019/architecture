if [ ! -d "deps" ]; then
  mkdir -p deps
  echo "Downloading spark dependencies"
  wget https://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.3.2/spark-2.3.2-bin-without-hadoop.tgz -P ./deps
else
  echo "Dependencies found, skipping retrieval..."
fi

docker build . -t newsparkbase
