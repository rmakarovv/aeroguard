# AeroGuard

Repository contains the pipeline for defect detection for aircrafts. The source code is in the [scripts](scripts) folder.

The pipeline consists of 3 stages:

### Preprocessing
[preprocess.cpp](scripts/preprocess.cpp) takes all the images from the input folder and converts them to black-and-white. The resulting images are saven into the output folder.

Usage example:
```
INPUT_DIR=/app/images_raw
OUTPUT_DIR=/app/images
/app/scripts/preprocess $(INPUT_DIR) $(OUTPUT_DIR)
```

### Processing
This is the detection stage. Script [process.py](scripts/process.py) takes the images from the images folder and runs them through two YOLO networks. The first one detects the defects and the bounding boxes. The second one classifies the detected defect into defect type classes. The weights for the models are stored in the [weights](weights) folder.

The script saves the images with the bounding boxes and defect classes drawn into the save folder by default.

Usage example:
```
INPUT_DIR=/app/images
OUTPUT_DIR=/app/save
DET_WEIGHTS=/app/weights/detector_wgts.pt
CLF_WEIGHTS=/app/weights/classifier_wgts.pt
python3 /app/scripts/process.py -d $(INPUT_DIR) -s $(OUTPUT_DIR) -dw $(DET_WEIGHTS) -cw $(CLF_WEIGHTS)
```

`-sb` option enables saving the bounding boxes.

If no command-line arguments are provided, the script reads them from the config.yaml file.

### Postprocessing
[postprocess.cpp](scripts/postprocess.cpp) takes all the images from the input folder and combines them into a single pdf report.

Usage example:
```
INPUT_DIR=/app/save
PDF_FILE=/app/output/processed_images.pdf
/app/scripts/postprocess $(INPUT_DIR) $(PDF_FILE)
```

## How to run

### Locally

```
make prereqs
make build
make -f scripts/Makefile all
```

### In a docker container

```
./build_container.sh
./run_container.sh
```

## Testing

### Locally
```
make prereqs
make build
make test_with_log
```

Or, if you want to save the testing results, substitute the last command for `make test`

### In a docker container

Comment the first line with the `ENTRYPOINT` in the [Dockerfile](Dockerfile), and uncomment the second one. Then run:

```
./build_container.sh
./run_container.sh
```

## Example outputs:

To discover the result of the run, look into [example_output/processed_images.pdf](https://github.com/rmakarovv/aeroguard/blob/fc0a7f927445b1d1376d35882bdb3a04953c3fb5/example_output/processed_images.pdf)
