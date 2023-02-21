# Writeup for the PicoCTF Challenge - Wireshark doo dooo do doo

```diff
+ completed the challenge
```

<!---
![Task](./assets/Screenshot%202023-02-19%20at%2011.41.48%20PM.png)
-->

Downloaded the file from this site and this was the first time in my life I had encountered a `.pcapng` file so I looked it up and found it to be some kind of next generation file format for storing web packets and that it had to be opened with a Software called `Wireshark` again I looked it up to understand what is Wireshark ;-; I found out that wireshark is used to analyse and collect network packet data so I visited the [Wireshark](https://www.wireshark.org) site to download it and found out this [video](https://youtu.be/lb1Dw0elw0Q) to learn Wireshark. Then I opened this file in Wireshark

![Terminal_open](./assets/Screenshot%202023-02-20%20at%201.16.10%20AM.png)
![Wireshark_open](./assets/Screenshot%202023-02-19%20at%2011.58.16%20PM.png)

Honestly I just randomly clicked on the first stream to follow the TCP stream and scrolled through it to find some random text in Stream 5

![Follow_stream](./assets/Screenshot%202023-02-20%20at%201.08.37%20AM.png)

Again my go to was `rot13` and I used it to decode the text to get this - `The flag is picoCTF{p33kab00_1_s33_u_deadbeef}`

![Get_flag](./assets/Screenshot%202023-02-20%20at%201.17.13%20AM.png)

## Links I referred to

-   https://www.wireshark.org
-   https://youtu.be/lb1Dw0elw0Q
-   https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/Wireshark%20doo%20dooo%20do%20doo/Wireshark%20doo%20dooo%20do%20doo.md
