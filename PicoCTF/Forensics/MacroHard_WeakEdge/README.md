# Writeup for the PicoCTF Challenge - MacroHard WeakEdge

```diff
+ completed the challenge
```

<!---
![Challenge](./assets/Screenshot%202023-02-20%20at%201.27.58%20AM.png)
-->

Downloaded the pptm file for the task from this site and tried opening it but it didn't open. Since I've worked with macro enabled ppts and excel sheets before, I know macro enabled files have a different extension. I tried to lookup on the internet for macro enabled ppts more and found that we can unzip them then I remembered how in the Cryptonite meeting the guy had hidden a virus inside a ppt so I directly tried unzipping the ppt using the `unzip` command

![Unzip](./assets/Screenshot%202023-02-20%20at%201.42.33%20AM.png)

In the files above ofc `slideMasters/hidden` seems the most sus file so I tried reading it's contents

![Cat_hidden](./assets/Screenshot%202023-02-20%20at%201.44.03%20AM.png)

I tried using `rot13` but it didn't work so I tried `base64` which for some reason didn't work for me after several attempts of doing it through the terminal so I finally resorted to an online site for it which decoded it and we found `flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}`

![Online_base64](./assets/Screenshot%202023-02-20%20at%201.56.57%20AM.png)

## Links used for additional information

-   https://dmfrsecurity.com/2021/08/24/picoctf-2021-macrohard-weakedge/
