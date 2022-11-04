#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t new_flask_docker .
docker run -p 5001:5001 -t new_flask_docker