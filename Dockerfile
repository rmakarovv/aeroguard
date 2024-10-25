FROM ubuntu:24.04

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

RUN mkdir /app/images
RUN mkdir /app/save
RUN mkdir /app/logs

COPY Makefile /app/Makefile
COPY requirements.txt /app/requirements.txt
RUN make prereqs

COPY scripts /app/scripts
RUN make build

COPY . /app/

RUN make test_with_log
ENTRYPOINT ["make", "-f", "scripts/Makefile", "all"]

# comment the previous entrypoint and RUN command and uncomment the following line if you want to just run unit tests
# ENTRYPOINT ["make", "test_with_log"]
