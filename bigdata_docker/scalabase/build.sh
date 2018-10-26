mkdir config
echo "Y" | ssh-keygen -t rsa -P '' -f config/id_rsa

if [ ! -d "deps" ]; then
  echo "Downloading scala"
  wget https://downloads.lightbend.com/scala/2.12.5/scala-2.12.5.tgz  -P ./deps
else
  echo "Dependencies found, skipping retrieval..."
fi

docker build . -t scalabase:latest