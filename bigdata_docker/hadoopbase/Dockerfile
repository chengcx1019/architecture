FROM scalabase


WORKDIR /home/hadoop


COPY deps/* /home/hadoop/
RUN tar -zxf hadoop-3.1.1.tar.gz
RUN mv hadoop-3.1.1 hadoop

RUN rm *.gz
RUN chown hadoop hadoop -R

RUN echo "export HADOOP_HOME=/home/hadoop/hadoop" >> /home/hadoop/.profile
RUN echo "export HADOOP_HOME=/home/hadoop/hadoop" >> /home/hadoop/.bashrc
RUN echo "export PATH=\$HADOOP_HOME/bin:\$HADOOP_HOME/sbin:\$PATH" >> /home/hadoop/.profile
RUN echo "export PATH=\$HADOOP_HOME/bin:\$HADOOP_HOME/sbin:\$PATH">> /home/hadoop/.bashrc
RUN mkdir -p /data/nameNode /data/dataNode /data/nameSecondary /data/tmp
RUN chown hadoop /data/nameNode /data/dataNode /data/nameSecondary /data/tmp



ENV HADOOP_HOME /home/hadoop/hadoop
# ENV HADOOP_PREFIX /home/hadoop/hadoop HADOOP_PREFIX has been replaced by HADOOP_HOME
ENV HADOOP_COMMON_HOME /home/hadoop/hadoop
ENV HADOOP_HDFS_HOME /home/hadoop/hadoop
ENV HADOOP_MAPRED_HOME /home/hadoop/hadoop
ENV HADOOP_YARN_HOME /home/hadoop/hadoop
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop
# ENV YARN_CONF_DIR $HADOOP_HOME/etc/hadoop YARN_CONF_DIR has been replaced by HADOOP_CONF_DIR

ENV PATH $HADOOP_HOME/bin:$PATH