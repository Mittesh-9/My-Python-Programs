from PIL import Image

# open the image file
img_path = r'C:\Users\Mittesh Waghule\Downloads\Mittesh.jpg'
img = Image.open(img_path)

# show the image as output
# img.show()

# define the new size
new_width = 750
new_height = 750

# resize the image
img_resized = img.resize((new_width, new_height))

# save the resized image (can also change the file type like png or something else)
img_resized.save(r'C:\Users\Mittesh Waghule\Downloads\resized_image.jpg')