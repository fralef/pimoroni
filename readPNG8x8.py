import unicornhat as unicorn

# sudo pip install pillow
from PIL import Image

# Load the image
image_path = 'image.png'
image = Image.open(image_path)
image = image.resize((8, 8))  # Resize the image to 8x8 pixels

# Initialize Unicorn HAT
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()

# Clear the Unicorn HAT
unicorn.clear()

image=image.convert("RGB")

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the RGB values of the pixel
        r, g, b = image.getpixel((x, y))

        # Set the pixel on the Unicorn HAT
        unicorn.set_pixel(x, y, r, g, b)

# Show the image on the Unicorn HAT
unicorn.show()
