From openjdk:8

USER root


RUN apt-get update \
	&& apt-get install -y --no-install-recommends openssh-server vim

WORKDIR /tmp
COPY ./deps/scala-2.12.5.tgz .
RUN tar xzf scala-2.12.5.tgz\
	&& mv scala-2.12.5 /usr/share/scala\
	&& ln -s /usr/share/scala/bin/* /usr/bin\
	&& rm scala-2.12.5.tgz

RUN echo PubkeyAuthentication yes >> /etc/ssh/ssh_config
RUN echo Host * >> /etc/ssh/ssh_config
RUN service ssh start
CMD service ssh start && bash


RUN useradd -m -s /bin/bash hadoop
WORKDIR /home/hadoop

RUN mkdir /home/hadoop/.ssh
RUN echo PubkeyAcceptedKeyTypes +ssh-dss >> /home/hadoop/.ssh/config
RUN echo PasswordAuthentication no >> /home/hadoop/.ssh/config

COPY config/id_rsa.pub /home/hadoop/.ssh/id_rsa.pub
COPY config/id_rsa /home/hadoop/.ssh/id_rsa
RUN cat /home/hadoop/.ssh/id_rsa.pub >> /home/hadoop/.ssh/authorized_keys
RUN chown hadoop .ssh -R
#RUN chmod 600 /home/hadoop/.ssh/id_rsa