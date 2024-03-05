import tifffile
import numpy as np
import glob
import os

# Path to the folder containing TIFF files
import argparse
parser = argparse.ArgumentParser(description='Stack TIFF files')
parser.add_argument('folder_path', type=str, help='Path to the folder containing TIFF files')
parser.add_argument('output_file', type=str, help='Path to the output TIFF file')
args = parser.parse_args()
folder_path = args.folder_path
output_file = args.output_file

# Get all TIFF files in the folder
tiff_files = sorted(glob.glob(os.path.join(folder_path, '*.tif')) + glob.glob(os.path.join(folder_path, '*.tiff')))

# Load and stack all TIFF files
images = [tifffile.imread(file) for file in tiff_files]
stacked_images = np.stack(images, axis=0)

# Make the directory if it does not exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save the stacked images as a new TIFF file
tifffile.imwrite(output_file, stacked_images)