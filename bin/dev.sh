#!/bin/bash
echo Starting
echo make sure you have a python environment activated
echo run: pip install -r requirements.txt

if [[ ! -d "$redishost" ]]; then 
    export redishost="localhost"
    echo 'export redishost="localhost"' >> ~/.bashrc
fi

docker kill redis
docker rm redis

if [[ ! -z $(docker images -q redis) ]]; then
	echo redis image exists
else 
  echo redis image does not exist
  docker pull redis
fi
docker network create -d bridge pkid-net
docker run --name redis --restart=always --network="pkid-net" -p 6379:6379 -d redis redis-server --appendonly yes

python run.py

docker kill redis
docker rm redis

echo finished