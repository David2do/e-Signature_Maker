
'''

This is the script that does the work. It accepts the signature image input and 
produces the output to be saved 

'''

# Import Packages
import cv2
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


# Initialize Tkinter and hide the root window
Tk().withdraw()

# Open a file dialog to select an image file
file_path = askopenfilename(title="Select the Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")])

# Check if a file was selected
if file_path:
    # Load the image using OpenCV
    sig_image = cv2.imread(file_path)
    
else:
    print("No file selected.")

# Convert to Grayscale.
sig_gray = cv2.cvtColor(sig_image, cv2.COLOR_BGR2GRAY)

# Create an Alpha Mask.
ret, alpha_mask = cv2.threshold(sig_gray, 150, 255, cv2.THRESH_BINARY_INV)

# Create a blue mask for blending.
blue_mask = sig_image.copy()
blue_mask[:, :] = (255, 0, 0)

# Blend the signature with the mask.
sig_color = cv2.addWeighted(sig_image, 1, blue_mask, 0.5, 0)

# Add the Alpha Mask as the 4th Channel to the Image.
# Split the color channels from the color image.
b, g, r = cv2.split(sig_color)
new = [b, g, r, alpha_mask]

# Use the merge() function to create a single, multi-channel array.
sig_png = cv2.merge(new, 4)

# Open the file dialog for saving the sig_png
save_file_path = filedialog.asksaveasfilename(defaultextension = ".png",
filetypes = [("PNG files","*.png")] )

if save_file_path :
    cv2.imwrite(save_file_path, sig_png)
    print("Successfully saved at", save_file_path)