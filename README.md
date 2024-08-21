# e-Signature_Maker
This program processes signature images by converting them to grayscale, creating an alpha mask, blending the image with a blue color mask, and saving the output as a PNG with transparency.

## Features
Converts signature images to grayscale.

Generates an alpha mask for transparency.

Blends the signature with a blue mask for styling.

Saves the processed signature image as a PNG with transparency.
## Requirements
Python 3.x

OpenCV (cv2)

Tkinter

Install dependencies with:

pip install opencv-python-contrib

Note: Tkinter is included with most Python installations. Ensure it is installed by default.

## How to Use
Run the Script:

When you execute the script, a file dialog will prompt you to select an image file (e.g., .jpg, .jpeg, .png, .bmp, .tiff).

Image Processing:

The selected image is loaded, converted to grayscale, and processed to create an alpha mask and a blue-colored blend.

Save the Output:

After processing, another file dialog will open, allowing you to save the processed signature image as a .png file.

## Usage Example
Clone the repository:

git clone https://github.com/your-username/e-Signature_Maker.git

Run the script:

python main.py

Select your signature image file and follow the prompts to save the processed image.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

*This project is intended to be updated with time. Addition of new features like advanced image processing, conversion to PDFs,
 and other key things are absolutely paramount to this project.*
