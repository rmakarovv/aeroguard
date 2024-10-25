.PHONY: prereqs build test test_with_log

prereqs: requirements.txt
	apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    imagemagick \
    libmagick++-dev \
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
	pip install -r requirements.txt --break-system-packages

build: ./scripts/preprocess.cpp ./scripts/postprocess.cpp
	g++ ./scripts/preprocess.cpp -o ./scripts/preprocess `pkg-config --cflags --libs opencv4`
	g++ ./scripts/postprocess.cpp -o ./scripts/postprocess `pkg-config --cflags --libs Magick++`

test: tests
	python3 -m unittest -v

test_with_log: ./tests/test_preprocessing.py ./tests/test_processing.py ./tests/test_postprocessing.py
	python3 ./tests/test_preprocessing.py
	python3 ./tests/test_processing.py
	python3 ./tests/test_postprocessing.py
