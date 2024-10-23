mkdir -p ./logs
mkdir -p ./images_raw
mkdir -p ./images
mkdir -p ./save
mkdir -p ./output

docker run -it --rm --name defect_detection_container \
    -v ./logs:/app/logs \
    -v ./images_raw:/app/images_raw \
    -v ./images:/app/images \
    -v ./save:/app/save \
    -v ./output:/app/output \
    defect_detection_image