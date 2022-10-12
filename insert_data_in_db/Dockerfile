FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install pymongo && pip3 install pandas
ADD footdbsetup.py /footdbsetup.py
ADD top250-00-19.csv /top250-00-19.csv
CMD python3 footdbsetup.py
