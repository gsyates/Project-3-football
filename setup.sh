#!/bin/bash

docker image build /home/ubuntu/Project-3-football/insert_data_in_db/. -t my_insert_data_in_db:latest

docker-compose up
