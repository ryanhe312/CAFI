import tifffile
import numpy as np
import glob
import os

# Path to the folder containing TIFF files
import argparse
parser = argparse.ArgumentParser(description='Split TIFF files')
parser.add_argument('input_file', type=str, help='Path to the input TIFF file')
parser.add_argument('folder_path', type=str, help='Path to the folder to store TIFF files')
args = parser.parse_args()
folder_path = args.folder_path
input_file = args.input_file

# Load the TIFF file
stacked_images = tifffile.imread(input_file)

# Create the folder if it does not exist
os.makedirs(folder_path, exist_ok=True)

# Save the stacked images as a new TIFF file
for i in range(stacked_images.shape[0]):
    tifffile.imwrite(os.path.join(folder_path, f'image_{i}.tif'), stacked_images[i])

# Print the number of images saved
print(f'{stacked_images.shape[0]} images saved to {folder_path}')