from handwritten_recognition import *
import argparse

# Get image path file from user
parser = argparse.ArgumentParser(description='Recognise digits in an image')

parser.add_argument('file_path', type=str,
                    help='Path to image')

args = parser.parse_args()

img_pth = args.file_path

# Load image
orig, gray = load_images(img_pth, show=False)

# Preprcess and crop out digits from image
cropped_digits = preprocess(gray,  6)

# Print recognized digits
show_digits(cropped_digits)
