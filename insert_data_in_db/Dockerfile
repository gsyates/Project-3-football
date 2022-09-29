FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install pymongo
ADD footdbsetup.py /footdbsetup.py
CMD python3 footdbsetup.py
