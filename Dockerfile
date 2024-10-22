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

RUN mkdir /app/images

# RUN g++ /app/scripts/preprocess.cpp -o /app/scripts/preprocess `pkg-config --cflags --libs opencv4`
# RUN /app/scripts/preprocess /app/images_raw /app/images

# RUN mkdir output

# RUN g++ /app/scripts/postprocess.cpp -o /app/scripts/postprocess `pkg-config --cflags --libs Magick++`
# RUN /app/scripts/postprocess /app/images /app/output/result.pdf

# Set the entry point
# ENTRYPOINT ["make", "-f", "/app/scripts/Makefile", "preprocess"]
