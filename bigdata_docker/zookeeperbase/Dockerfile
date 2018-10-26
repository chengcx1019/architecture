From scalabase

WORKDIR /home/hadoop

COPY ./deps/zookeeper-3.4.13.tar.gz .
RUN tar xzf zookeeper-3.4.13.tar.gz\
	&& mv zookeeper-3.4.13 zookeeper\
	&& ln -s zookeeper/bin/* /usr/bin\
	&& rm zookeeper-3.4.13.tar.gz


RUN mkdir -p zoo/data
RUN mkdir -p zoo/log

# Env zookeeper
RUN echo "export ZOOKEEPER_HOME=/home/hadoop/zookeeper" >> /home/hadoop/.bashrc
RUN echo "export ZOOKEEPER_HOME=/home/hadoop/zookeeper" >> /home/hadoop/.profile
RUN echo "export PATH=\$PATH:\$ZOOKEEPER_HOME/bin" >> /home/hadoop/.bashrc
RUN echo "export PATH=\$PATH:\$ZOOKEEPER_HOME/bin" >> /home/hadoop/.profile

RUN chown hadoop /home/hadoop/.profile /home/hadoop/.bashrc

ENV ZOOKEEPER_HOME /home/hadoop/zookeeper
ENV PATH $PATH:$ZOOKEEPER_HOME/bin
ENV TZ "Asia/Shanghai"
EXPOSE 2181 2888 3888

RUN /bin/bash -c "source /home/hadoop/.bashrc"


CMD ["zkServer.sh", "start-foreground"]