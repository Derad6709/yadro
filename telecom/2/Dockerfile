FROM ubuntu:22.04

COPY ../1/main.py ../1/requirements.txt /
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "/main.py" ]