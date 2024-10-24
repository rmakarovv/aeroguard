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

# docker run -it -v C:/Users/r.makarov/OneDrive/Skoltech/SE/aeroguard/output:/app/output -v C:/Users/r.makarov/OneDrive/Skoltech/SE/aeroguard/logs:/app/logs -v C:/Users/r.makarov/OneDrive/Skoltech/SE/aeroguard/save:/app/save -v C:/Users/r.makarov/OneDrive/Skoltech/SE/aeroguard/images:/app/images defect_detection_image