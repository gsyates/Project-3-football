FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install flask && pip3 install requests && pip3 install pandas
ENV LOG=1
COPY test_api.py test_api.py
CMD python3 test_api.py
