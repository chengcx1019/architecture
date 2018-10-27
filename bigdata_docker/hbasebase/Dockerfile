FROM newsparkbase

WORKDIR /home/hadoop

COPY ./deps/* /home/hadoop/
RUN tar -zxf hbase-2.1.0-bin.tar.gz
RUN rm *.gz
RUN mv hbase-2.1.0 hbase
RUN chown hadoop hbase -R

ENV HBASE_HOME=/home/hadoop/hbase
ENV PATH=$PATH:$HBASE_HOME/bin

RUN echo "export HBASE_HOME=/home/hadoop/hbase" >> /home/hadoop/.bashrc
RUN echo "export HBASE_HOME=/home/hadoop/hbasep" >> /home/hadoop/.profile
RUN echo "export PATH=\$PATH:\$HBASE_HOME/bin" >> /home/hadoop/.bashrc
RUN echo "export PATH=\$PATH:\$HBASE_HOME/bin" >> /home/hadoop/.profile


# Hdfs ports
EXPOSE 9000 50010 50020 50070 50075 50090
# See https://issues.apache.org/jira/browse/HDFS-9427
EXPOSE 9871 9870 9820 9869 9868 9867 9866 9865 9864
# Mapred ports
EXPOSE 19888
#Yarn ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088 8188
#Other ports
EXPOSE 49707 2122
