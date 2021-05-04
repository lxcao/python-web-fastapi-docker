###
 # @Author: clingxin
 # @Date: 2021-05-04 09:50:18
 # @LastEditors: clingxin
 # @LastEditTime: 2021-05-04 09:56:32
 # @FilePath: /python-web-fastapi-docker/setup.sh
###

apt update && apt upgrade -y
apt install -y -q build-essential python3-pip python3-dev
pip3 install -U pip setuptools wheel
pip3 install gunicorn uvloop httptools

cp .requirements.txt /app/requirements.txt

pip3 install -r /app/requirements.txt

cp ./service/ /app

/usr/local/bin/gunicorn \
    -b 0.0.0.0 80 \
    -w 4 \
    -k uvicorn.works.UvicornWorker main:app


