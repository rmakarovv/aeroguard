IMAGES_RAW_DIR=images_raw
IMAGES_DIR=images
OUTPUT_DIR=output
PDF_FILE=processed_images.pdf

all: preprocess process postprocess

preprocess:
	echo "Preprocessing images..."
	/app/scripts/preprocess $(IMAGES_RAW_DIR) $(IMAGES_DIR)

process:
	echo "Running NN processing..."
	python3 process.py $(IMAGES_DIR) $(OUTPUT_DIR)

postprocess:
	echo "Generating PDF from processed images..."
	/app/scripts/postprocess $(OUTPUT_DIR) $(PDF_FILE)

clean:
	rm -rf $(IMAGES_DIR)/* $(OUTPUT_DIR)/* $(PDF_FILE)