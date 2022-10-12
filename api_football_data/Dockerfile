FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install pymongo && pip3 install pandas && pip3 install flask && pip3 install requests
ENV LOG=1
CMD export FLASK_DEBUG=1
COPY server.py server.py
EXPOSE 8000
CMD python3 server.py
