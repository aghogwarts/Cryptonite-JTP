# Writeup for the PicoCTF Challenge - Pixelated

```diff
+ completed the challenge

- had no idea what to do so took internet help
```

Apparently I could easily combine two images using Stegsolve of which I couldn't find a MacOS version again oh god. Then I saw another solution which is far more efficient and I can use numpy to combine the image data of the images and convert it into a image and save it

```py
from PIL import Image
import numpy as np

img1 = Image.open("./scrambled1.png")
img2 = Image.open("./scrambled2.png")

img1_data = np.asarray(img1)
img2_data = np.asarray(img2)

data = img1_data.copy() + img2_data.copy()

new_image = Image.fromarray(data)
new_image.save("out.png", "PNG")
```

So I understood the challenge and completed it

## Links I referred to

-   https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Cryptography/Pixelated/Pixelated.md
-   https://www.julianhal.com/picoctf/pixelated/
