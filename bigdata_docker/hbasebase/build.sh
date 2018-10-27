if [ ! -d "deps" ]; then
  mkdir -p deps
  echo "Downloading hbase dependencies"
  wget http://apache.claz.org/hbase/2.1.0/hbase-2.1.0-bin.tar.gz  -P ./deps
else
  echo "Dependencies found, skipping retrieval..."
fi

docker build . -t hbasebase
