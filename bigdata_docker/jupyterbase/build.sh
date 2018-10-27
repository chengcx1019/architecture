#!/usr/bin/env bash
if [ ! -d ".pyenv" ]; then
  echo "Downloading pyenv, pyenv-virtuals"
  git clone https://github.com/pyenv/pyenv.git .pyenv
  git clone https://github.com/pyenv/pyenv-virtualenv.git .pyenv/plugins/pyenv-virtualenv
else
  echo "Dependencies found, skipping retrieval..."
fi

docker build . -t jupyterbase
