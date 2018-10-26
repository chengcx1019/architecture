FROM hadoopbase

WORKDIR /home/hadoop

ENV HIVE_HOME=/home/hadoop/hive

COPY deps/* /home/hadoop/
RUN tar -zxf apache-hive-3.1.0-bin.tar.gz  && \
     mv apache-hive-3.1.0-bin hive && \
     rm apache-hive-3.1.0-bin.tar.gz

RUN tar -zxf mysql-connector-java-5.1.39.tar.gz  && \
    mv mysql-connector-java-5.1.39/mysql-connector-java-5.1.39-bin.jar $HIVE_HOME/lib/ && \
    rm -rf mysql-connector-java-5.1.39 && \
    rm mysql-connector-java-5.1.39.tar.gz

RUN mkdir -p /home/hadoop/data/hive/warehouse && mkdir -p /home/hadoop/data/hive/log

ENV PATH=$PATH:$HIVE_HOME/bin

RUN echo "export HIVE_HOME=/home/hadoop/hive" >> /home/hadoop/.profile
RUN echo "export HIVE_HOME=/home/hadoop/hive">> /home/hadoop/.bashrc
RUN echo "export PATH=\$PATH:\$HIVE_HOME/bin" >> /home/hadoop/.profile
RUN echo "export PATH=\$PATH:\$HIVE_HOME/bin">> /home/hadoop/.bashrc



