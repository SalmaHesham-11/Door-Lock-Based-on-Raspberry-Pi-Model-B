#Libraries needed in code
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
from RPLCD.gpio import CharLCD
from RPLCD import cleared
from RPLCD import cursor
import RPi.GPIO as GPIO
import time

lcd = CharLCD(numbering_mode = GPIO.BOARD,cols=16, rows=2, pin_rs=7, pin_e=11, pins_data=[19.21.13.15])
#pins_data==> from D0 to D7

while True:
    #clock animation
    lcd.write_string(u' Welcome to   ClockPi')

  


  #display clock symbol using pixles

    clock1 = (
        0b00000,
        0b11111,
        0b10011,
        0b10101,
        0b10001,
        0b11111,
        0b00000,
        0b00000,
    )
    #create and save 1st clock symbol
    lcd.create_char(0, clock1)
    #calling it
    lcd.write_string(chr(0))
    #it take is displaying it on screen
    time.sleep(1)
    #clear lcd screen
    lcd.clear()

    
lcd.write_string(u' welcome to clockPI ')
    clock2 = (
        0b00000,
        0b11111,
        0b10001,
        0b10101,
        0b10011,
        0b11111,
        0b00000,
        0b00000,
        )
    #creat and save 2nd clock symbol
    lcd.create_char(1, clock2)
    #calling it again as we did in 1st one
    lcd.write_string(chr(1))
    #it take 1s displaying it on screen
    time.sleep(1)
    #clear lcd screen
    lcd.clear()
    #repeated steps


    lcd.write_string(u' welcome to clockPI ')
    clock3 = (
        0b00000,
        0b11111,
        0b10001,
        0b10101,
        0b11001,
        0b11111,
        0b00000,
        0b00000,
        )
    #creat and save 2nd clock symbol
    lcd.create_char(2, clock3)
    #calling it again as we did in 1st one
    lcd.write_string(chr(2))
    #it take 1s displaying it on screen
    time.sleep(1)
    lcd.clear()


   

 lcd.write_string(u' welcome to clockPI ')
    clock4 = (
    0b00000,
    0b11111,
    0b10001,
    0b10101,
    0b10011,
    0b11111,
    0b00000,
    0b00000,
    )
    #creat and save 2nd clock symbol
    lcd.create_char(3, clock4)
    #calling it again as we did in 1st one
    lcd.write_string(chr(3))
    #it take 1s displaying it on screen
    time.sleep(1)
    #clear lcd screen
    lcd.clear()
    #repeated steps
    

lcd.write_string(u' welcome to clockPI ')
    clock5 = (
            0b00000,
            0b11111,
            0b10001,
            0b10101,
            0b11001,
            0b11111,
            0b00000,
            0b00000,
            )

    lcd.create_char(0, clock5)
    lcd.write_string(chr(0))
    time.sleep(1)
    lcd.clear()




   

 #display Dr name
    lcd.write_string(u'Dr.fouda')
    #display it for 6s
    time.sleep(6)
    #clear lcd screen 
    lcd.clear()


    #display our names
    lcd.write_string(u'Salma hesham 3')
    lcd.write_string(u'Mariam Lotfy 3')
    #display it for 5s
    time.sleep(5)
    lcd.clear()

    lcd.write_string(u'Abdulrahman\n\rSnad       3')
    time.sleep(5)
    lcd.clear()

    lcd.write_string(u'Saif-Eddin 3')
    lcd.write_string(u'Mahmoud Allam  3')
    time.sleep(5)
    lcd.clear()

    #to stop the loop
    break
    #time and date
    #new loop for time and date infinity loop
for x in range(15):
    #to show time >> hours : minutes : seconds
    lcd.write_string("time:%s"%time.strftime("%H:%M:%S"))
    #show it in first row
    lcd.cursor_pos=(1,0)
    #to show time >> day : month :year
    lcd.write_string("date:%s"%time.strftime("%d:%m:%Y"))
    #refresh every second
    time.sleep(1)
    #clear the screen every second
    lcd.clear()



#set gpio for key pad

ROW = [23,12,16,18]
COL = [22,24,26,3]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)
    
for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# set gpio for servo   
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(5)






#Function to check keypad input!
def check_keypad(length):

ROW = [23,12,16,18]
COL = [22,24,26,3]

    MATRIX = [["1","2","3","A"],
              ["4","5","6","B"],
              ["7","8","9","C"],
              ["0","F","E","D"]]
    result = ""
    while(True):
        for j in range(4):
            GPIO.output(COL[j], 0)

            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    time.sleep(0.02)
                    result = result + MATRIX[i][j]
                    while(GPIO.input(ROW[i]) == 0):
                          time.sleep(0.02)

            GPIO.output(COL[j], 1)
            if len(result) >= length:
                return result

# password
password = "A1234"
length = len(password)

#Password From KeyPad


lcd.write_string('u Please Enter User Password: ')
result = check_keypad(length)


#Password Check
if result == password:
    lcd.write_string('u Unlock ')
    pwm.ChangeDutyCycle(10)

else:
    lcd.write_string("Try Agian")  
