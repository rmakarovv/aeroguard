.PHONY: prereqs build test test_with_log

prereqs: requirements.txt
	pip install -r requirements.txt --break-system-packages

build: /app/scripts/preprocess.cpp /app/scripts/postprocess.cpp
	g++ /app/scripts/preprocess.cpp -o /app/scripts/preprocess `pkg-config --cflags --libs opencv4`
	g++ /app/scripts/postprocess.cpp -o /app/scripts/postprocess `pkg-config --cflags --libs Magick++`

test: tests
	python3 -m unittest -v

test_with_log: /app/tests/test_preprocessing.py /app/tests/test_processing.py /app/tests/test_postprocessing.py
	python3 /app/tests/test_preprocessing.py
	python3 /app/tests/test_processing.py
	python3 /app/tests/test_postprocessing.py
