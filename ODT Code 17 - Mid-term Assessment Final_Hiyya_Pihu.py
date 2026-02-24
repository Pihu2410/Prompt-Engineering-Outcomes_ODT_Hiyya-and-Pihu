#ODT mid-term assessment
#Hiyya & Pihu
#Reaction time game

from machine import TouchPad, Pin
import time
import random

t1 = TouchPad(Pin(15))
t2 = TouchPad(Pin(27))
t3 = TouchPad(Pin(4))
t4 = TouchPad(Pin(13))
t5 = TouchPad(Pin(12))
t6 = TouchPad(Pin(14))

led1=Pin(26, Pin.OUT)
led2=Pin(25, Pin.OUT)
led3=Pin(33, Pin.OUT)
led4=Pin(32, Pin.OUT)
led5=Pin(22, Pin.OUT)
led6=Pin(23, Pin.OUT)

score=0
count=0

led1.off()
led2.off()
led3.off()
led4.off()
led5.off()
led6.off()
time.sleep(2)

#randomly choose 1 LED out of the 6 available LEDs to light up for a small fixed duration (1200 ms)
#repeat this 10 times
#while an LED is lit, check for touch on the touchpad corresponding to that LED
#if touched correctly, score is increased

while(count<10):
    startTime=time.ticks_ms()
    led_lit = random.randint(1, 6)
    print (led_lit)
    
    while(1):
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
        led6.off()
        
        if (led_lit==1):
            led1.on()
            currentTime=time.ticks_ms()
            touchValue1=t1.read()
            if(touchValue1<300):
              score = score + 1  
            if(time.ticks_diff(currentTime, startTime)>380):
                count = count+1
                break
    
        if (led_lit==2):
            led2.on()
            currentTime=time.ticks_ms()
            touchValue2=t2.read()
            if(touchValue2<300):
              score = score + 1  
            if(time.ticks_diff(currentTime, startTime)>380):
                count = count+1
                break
    
        if (led_lit==3):
            led3.on()
            currentTime=time.ticks_ms()
            touchValue3=t3.read()
            if(touchValue3<300):
              score = score + 1  
            if(time.ticks_diff(currentTime, startTime)>380):
                count = count+1
                break
    
        if (led_lit==4):
            led4.on()
            currentTime=time.ticks_ms()
            touchValue4=t4.read()
            if(touchValue4<300):
              score = score + 1  
            if(time.ticks_diff(currentTime, startTime)>380):
                count = count+1
                break
    
        if (led_lit==5):
            led5.on()
            currentTime=time.ticks_ms()
            touchValue5=t5.read()
            if(touchValue5<300):
              score = score + 1  
            if(time.ticks_diff(currentTime, startTime)>380):
                count = count+1
                break
    
        if (led_lit==6):
            led6.on()
            currentTime=time.ticks_ms()
            touchValue6=t6.read()
            if(touchValue6<300):
              score = score + 1  
            if(time.ticks_diff(currentTime, startTime)>380):
                count = count+1
                break
            
led1.off()
led2.off()
led3.off()
led4.off()
led5.off()
led6.off()
print (score)

#for low score (poor performance/high reaction time), red lights turn on
#for medium score (average reaction time), blue lights turn on
#for high score (good performance/low reaction time), green lights turn on

if score<1500:
    led3.on()
    led5.on()
elif score>3000:
    led1.on()
    led2.on()
else:
    led4.on()
    led6.on()
    
            
