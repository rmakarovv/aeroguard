IMAGES_RAW_DIR=images_raw
IMAGES_DIR=images
OUTPUT_DIR=save
PDF_FILE=output/processed_images.pdf

all: preprocess process postprocess

preprocess:
	echo "Preprocessing images..."
	/app/scripts/preprocess $(IMAGES_RAW_DIR) $(IMAGES_DIR)

process:
	echo "Running NN processing..."
	python3 /app/scripts/process.py

postprocess:
	echo "Generating PDF from processed images..."
	/app/scripts/postprocess $(OUTPUT_DIR) $(PDF_FILE)

clean:
	rm -rf $(IMAGES_DIR)/* $(OUTPUT_DIR)/* $(PDF_FILE)