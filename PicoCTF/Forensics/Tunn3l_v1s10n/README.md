# Writeup for the PicoCTF Challenge - tunn3l v1s10n

```bash
$completed this task with some help
```

![Challenge](./assets/Screenshot%202023-02-19%20at%206.53.03%20PM.png)

I downloaded the file from the site above and tried opening it but turns out it's just a collection of data in hex

![Opening_File](./assets/Screenshot%202023-02-19%20at%206.54.38%20PM.png)

I then tried opening this file using a app called `HextEdit` from the App Store

![Opening_Hex](./assets/Screenshot%202023-02-19%20at%207.29.04%20PM.png)

As you see the header of the file starts with BM indicating it's a Bitmap file format so I copied and renamed the file to `tunn3l_v1s10n.bmp` and tried opening it

![Opening_Bmp](./assets/Screenshot%202023-02-19%20at%207.32.51%20PM.png)

Okay so this doesn't work and I guess the file might be corrupted so I reopen the `.bmp` renamed file with the Hex Editor.
Reading this ![Wikipedia](https://en.wikipedia.org/wiki/BMP_file_format) link I find that the hex values in the header are corrupted (showing some letter combinations for example BA D0). I didn't find a way to proceed further so I took help of this ![article](https://hackmd.io/@UHzVfhAITliOM3mFSo6mfA/rJt5yM26s) to change the values to `38 00` and `28 00` respectively

![Changing_hex](./assets/Screenshot%202023-02-19%20at%208.57.15%20PM.png)

Now I tried opening this bitmap image

![Open_bmp](./assets/Screenshot%202023-02-19%20at%208.57.03%20PM.png)

As the article says the size of the image seemed pretty off from the likes of the image I could see so it might be larger then I changed the hex with the height value

![Change_hex](./assets/Screenshot%202023-02-19%20at%208.59.02%20PM.png)

Now opening the bitmap image we get the actual flag `picoCTF{qu1t3_a_v13w_2020}`

![Open_flag](./assets/Screenshot%202023-02-19%20at%208.58.52%20PM.png)

## Links I referred to

https://en.wikipedia.org/wiki/BMP_file_format
https://www.youtube.com/watch?v=X4kJiQdDn7M
https://hackmd.io/@UHzVfhAITliOM3mFSo6mfA/rJt5yM26s
https://coolconversion.com/math/binary-octal-hexa-decimal
