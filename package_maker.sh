#!/usr/bin/sh

CONTGENERATOR=./container_gen/container_generator.py
SPECIAL_CONTAINER=./container_gen/spe_containers.py
CONTAINERS_FILE=./pynohtml/containers.py

python $CONTGENERATOR -f $CONTAINERS_FILE
cat $SPECIAL_CONTAINER >> $CONTAINERS_FILE