#include <opencv2/opencv.hpp>
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

void convertToGrayscale(const std::string& inputPath, const std::string& outputPath) {
    cv::Mat img = cv::imread(inputPath, cv::IMREAD_COLOR);
    if (img.empty()) {
        std::cerr << "Could not open or find the image: " << inputPath << std::endl;
        return;
    }

    cv::Mat grayImg;
    cv::cvtColor(img, grayImg, cv::COLOR_BGR2GRAY);
    cv::imwrite(outputPath, grayImg);
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "Usage: preprocess_images <input_raw_dir> <input_dir>" << std::endl;
        return -1;
    }

    std::string inputRawDir = argv[1];
    std::string inputDir = argv[2];

    for (const auto& entry : fs::directory_iterator(inputRawDir)) {
        std::string inputPath = entry.path().string();
        std::string outputPath = inputDir + "/" + entry.path().filename().string();

        convertToGrayscale(inputPath, outputPath);
    }

    return 0;
}