FROM ubuntu:latest

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
    libopencv-dev

WORKDIR /app

COPY scripts /app/scripts
COPY images_raw /app/images_raw
COPY input_data /app/input_data
COPY tests /app/tests
COPY weights /app/weight
COPY Makefile /app/Makefile

RUN mkdir /app/images
RUN mkdir /app/save

# Set the entry point
# ENTRYPOINT ["make", "-f", "/app/scripts/Makefile", "preprocess"]
