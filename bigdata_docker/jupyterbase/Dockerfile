FROM scalabase:latest

USER root

WORKDIR /
COPY .pyenv /.pyenv/
RUN touch pyenv.sh
RUN echo 'export PYENV_ROOT="/.pyenv"' >> pyenv.sh
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> pyenv.sh
RUN echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> pyenv.sh
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> pyenv.sh
RUN mv pyenv.sh /etc/profile.d/

# RUN /bin/bash -c "pyenv versions"
ENV build_deps='make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev'
RUN apt-get update\
	&& apt-get install -y --no-install-recommends $build_deps
COPY ./deps/Python-3.5.6.tar.xz /.pyenv/cahce/
COPY ./data/requirement.txt .
RUN /bin/bash -c "source /etc/profile \
	&& pyenv install 3.5.6 \
	&& pyenv global 3.5.6 \
	&& pyenv virtualenv 3.5.6 spark \
	&& pyenv global spark \
	&& pip install -r /requirementtxt /"
rm requirement.txt
RUN apt-get purge -y --auto-remove $build_deps

# pyenv
RUN chown hadoop /.pyenv -R
RUN cat /etc/profile.d/pyenv.sh | tee -a /home/hadoop/.profile
RUN cat /etc/profile.d/pyenv.sh | tee -a /home/hadoop/.bashrc

RUN mkdir -p devlop/data
RUN chown hadoop devlop -R
 "nohup jupyter notebook --ip hadoop-jupyter --port 9312 &"

RUN /bin/bash -c "su hadoop \
    && source /home/hadoop/.bashrc\
	&& pyenv global spark\
	&& cd /home/hadoop/deploy \
	&& nohup jupyter notebook --ip hadoop-jupyter --port 9312 &"