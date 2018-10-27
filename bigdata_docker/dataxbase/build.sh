if [! -d "deps" ]; then
    echo "Downloading dataX"
        wget http://datax-opensource.oss-cn-hangzhou.aliyuncs.com/datax.tar.gz -P ./deps/
else
    echo "Dependencies found, skipping retrieval..."
fi

docker build . -t dataxbase