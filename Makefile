.PHONY: prereqs build test test_with_log

prereqs: requirements.txt
	pip install -r requirements.txt

build: /app/scripts/preprocess.cpp /app/scripts/postprocess.cpp
	g++ /app/scripts/preprocess.cpp -o /app/scripts/preprocess `pkg-config --cflags --libs opencv4`
	g++ /app/scripts/postprocess.cpp -o /app/scripts/postprocess `pkg-config --cflags --libs Magick++`

test: tests
	python -m unittest -v

test_with_log: tests/test_preprocessing.py tests/test_processing.py tests/test_postprocessing.py
	python tests/test_preprocessing.py
	python tests/test_processing.py
	python tests/test_postprocessing.py