#include <iostream>
#include <filesystem>
#include <Magick++.h>

namespace fs = std::filesystem;

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <input_directory> <output_pdf>" << std::endl;
        return 1;
    }

    std::string input_dir = argv[1];
    std::string output_pdf = argv[2];

    try {
        Magick::InitializeMagick(*argv);

        std::vector<Magick::Image> images;
        for (const auto& entry : fs::directory_iterator(input_dir)) {
            std::string img_path = entry.path().string();
            
            Magick::Image img(img_path);

            images.push_back(img);
        }

        // Save all resized images into a single PDF
        Magick::writeImages(images.begin(), images.end(), output_pdf);
        std::cout << "PDF created successfully with resized images: " << output_pdf << std::endl;
    } catch (std::exception& e) {
        std::cerr << "Error creating PDF: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}