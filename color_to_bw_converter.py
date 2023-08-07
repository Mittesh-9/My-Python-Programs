import sys
from PIL import Image

def convert_to_bw(input_file, output_file):
    try:
        image = Image.open(input_file)
    except IOError:
        print("Could not open file:", input_file)
        sys.exit(1)

    bw_image = image.convert("L")  # Convert to grayscale

    try:
        bw_image.save(output_file)
        print("Image converted to black and white and saved as", output_file)
    except Exception as e:
        print("Error saving image:", e)

if len(sys.argv) != 3:
    print("Usage: python converter.py <input_image> <output_image>")
    sys.exit(1)

input_image = sys.argv[1]
output_image = sys.argv[2]

# To succesfully run this code type input as this in the terminal : python color_to_bw_converter.py courage_the_cowardly_dog.jpg Output_courage.jpg 

convert_to_bw(input_image, output_image)