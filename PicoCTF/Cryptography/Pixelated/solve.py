from PIL import Image
import numpy as np

# Open image files
img1 = Image.open("./scrambled1.png")
img2 = Image.open("./scrambled2.png")

# Store the image data in an array
img1_data = np.asarray(img1)
img2_data = np.asarray(img2)

# Add both image data to combine
data = img1_data.copy() + img2_data.copy()

# Convert combined data to image and save the image
new_image = Image.fromarray(data)
new_image.save("flag.png", "PNG")
