#!/bin/bash

docker image build /home/ubuntu/Project-3-football/insert_data_in_db/. -t my_insert_data_in_db:latest

docker image build /home/ubuntu/Project-3-football/api_football_data/. -t launchfootballapi:latest

docker image build /home/ubuntu/Project-3-football/test_football_api/. -t testfootballapi:latest

docker-compose up
