from PIL import Image, ImageEnhance, ImageFilter
import os

path  = r"e:\image to be edited"
path_out = r"e:\edited image"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    edit = img.filter(ImageFilter.SHARPEN).convert("L")

    clean_name = os.path.splitext(filename)[0]

    # edit.save(f".{path_out}/{clean_name}_edited.png") This does not work on windows
    edit.save(os.path.join(path_out, f"{clean_name}_edited.png"))