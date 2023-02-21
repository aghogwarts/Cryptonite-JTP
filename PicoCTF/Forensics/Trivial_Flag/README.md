# Writeup for the PicoCTF Challenge - Trivial Flag Transfer Protocol

```diff
+ understood everything about the task

- couldn't complete it due to the lack of a MacOS version of steghide
```

![Task](./assets/Screenshot%202023-02-20%20at%202.00.16%20AM.png)

Downloaded the files for the task from this site and opened it using wireshark because it was a packet file

![Terminal_Wireshark](./assets/Screenshot%202023-02-20%20at%202.26.46%20AM.png)
![Wireshark_ss](./assets/Screenshot%202023-02-20%20at%202.26.56%20AM.png)

The name of the challenge fits the acronym TFTP so i tried exporting the files from the TFTP Protocol

![Export](./assets/Screenshot%202023-02-20%20at%202.27.19%20AM.png)

I then navigated to the folder of my Task and listed the files to find a instructions.txt which seemed to contain letters encoding something definitely so of the common two `rot13` and `base64` encryption methods, I tried decoding using rot13 with it's alias command I had created. <br>

`IWILLCHECKBACKFORTHEPLAN` suggested me to try opening the file named plan so I again found out random text which I tried running the `rot13` method again which surprisingly worked lol I didn't expect a repeat of the same algo. <br>

`IUSEDTHEPROGRAM` indicated I should try opening the program debian file which I couldn't on MacOS so I used internet help to look over this [article](https://dmfrsecurity.com/2021/09/05/picoctf-trivial-flag-transfer-protocol-writeup/) for the solution of this task.

`CHECKOUTTHEPHOTOS` well I did and since I remember the mention of steganography in the slides of the Cryptonite meeting and the article linked above showed how the `program.deb` shows mention of a tool called Steghide I looked it up and found no version of it for my OS. So I gave up and read the article to proceed further. Although I understood the task and completed it in my mind.

![Finding_Flag](./assets/Screenshot%202023-02-20%20at%202.31.34%20AM.png)

## Links I referred to

-   https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol
-   https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/Trivial%20Flag%20Transfer%20Protocol/Trivial%20Flag%20Transfer%20Protocol.md
-   https://dmfrsecurity.com/2021/09/05/picoctf-trivial-flag-transfer-protocol-writeup/
