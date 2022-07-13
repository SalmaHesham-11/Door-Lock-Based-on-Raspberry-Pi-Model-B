# Door-Lock-Based-on-Raspberry-Pi-Model-B
## Raspberry Pi Model B 2011.12 pins
![image](https://user-images.githubusercontent.com/76129033/178801626-d5de2830-9c7a-4979-804f-47576ffac40e.png)
![image](https://user-images.githubusercontent.com/76129033/178801685-700b642f-d89d-4ef5-b85e-b1d7dab6c40e.png)


## LCD 1602
![image](https://user-images.githubusercontent.com/76129033/178802165-528e09b1-ad03-4985-9a6d-860b30195026.png)
![image](https://user-images.githubusercontent.com/76129033/178802187-e0f94c78-dc64-4f90-937b-8f0ff206da96.png)


## keypad
![image](https://user-images.githubusercontent.com/76129033/178802411-233681c7-f667-4e8e-9a51-16bfb7d0d696.png)
![image](https://user-images.githubusercontent.com/76129033/178803804-4ab4aeea-950e-46d8-9c8a-693134162e05.png)


## connection:
1.	Connect the VDD on the LCD with pin number 2 on Raspberry Pi (+5v).
2.	Connect the VSS on the LCD with pin number 6 on Raspberry Pi (Ground).
3.	Then put 10k Ohm variable resistance to control contrast of the LCD connecting the VE pin on the LCD (control contrast) with the center pin of one resistance and one of the other pins with the ground.
4.	Connect the RS pin on the LCD with GPIO pin number 7 on the Raspberry Pi pins.
5.	Connect the RW pin on the LCD with ground.
6.	Connect the E pin on the LCD with GPIO pin number 11 on the Raspberry Pi pins.
7.	Connect the data pins from D0 to D4 on the LCD with GPIO pins on the Raspberry Pi

```
LCD pins	   GPIO pins
  D0	              19
  D1	              21
  D2	              13
  D3	              15
```
 
8.Then put another variable 10k Ohm resistance to control brightness of the LCD connecting the A pin on the LCD (control brightness) with the center pin of the resistance and one of the other pins with the +5v.

9.Connect the K pin on the LCD (control brightness) with the ground.

 ```
 Keypad pin	GPIO	      keypad	GPIO
    ROWS	                         COLUMMS
    1	      23	               5	  22
    2	      12	               6	  24
    3	      16	               7	  26
    4	      18	               8	  3
```
