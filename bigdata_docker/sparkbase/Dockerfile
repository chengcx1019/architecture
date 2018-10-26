FROM hivebase:latest

EXPOSE 22/tcp
EXPOSE 22/udp


WORKDIR /home/hadoop

COPY ./deps/* /home/hadoop/
COPY conf/sparkcmd.sh /home/hadoop/
RUN tar -zxf spark-2.3.2-*.tgz
RUN rm *.tgz
RUN mv spark-2.3.2-* spark
RUN chown hadoop spark -R


# Spark
RUN echo "export HADOOP_CONF_DIR=/home/hadoop/hadoop/etc/hadoop" >> /home/hadoop/.bashrc
RUN echo "export HADOOP_CONF_DIR=/home/hadoop/hadoop/etc/hadoop" >> /home/hadoop/.profile
RUN echo "export SPARK_DIST_CLASSPATH=\$(hadoop classpath)" >> /home/hadoop/.bashrc
RUN echo "export SPARK_DIST_CLASSPATH=\$(hadoop classpath)" >> /home/hadoop/.profile
RUN echo "export SPARK_HOME=/home/hadoop/spark" >> /home/hadoop/.profile
RUN echo "export SPARK_HOME=/home/hadoop/spark" >> /home/hadoop/.bashrc


ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin:.

RUN chown hadoop /home/hadoop/*


