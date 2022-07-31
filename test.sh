#!/bin.bash

docker-compose up -d
docker exec -it Backend sh -c "pytest tests/"

