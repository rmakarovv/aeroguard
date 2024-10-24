FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    imagemagick \
    libmagick++-dev \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    libjpeg-dev \
    libtiff-dev \
    libpng-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk-3-dev \
    libatlas-base-dev \
    gfortran \
    libopencv-dev \
    vim

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

ENTRYPOINT ["make", "-f", "scripts/Makefile", "all"]

# comment the previous entrypoint and uncomment the following line if you want to run unit tests
# ENTRYPOINT ["make", "test_with_log"]
