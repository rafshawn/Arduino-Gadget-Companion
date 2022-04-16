# Lab Mini Project
# Shawn Adrian (201830718)
# ENGI-1020

# Modules
# ---------------------------------------------------------

from engi1020.arduino import *
from time import *
import random

# Function Definitions
# ---------------------------------------------------------

# Initial screen on the LCD before any interaction
def startScreen(d1, button):
    while button == False:
        button
    
        lcd_hsv(0,1,255)
        lcd_clear()
        lcd_print("Hold button to s")
        sleep(1)
        if digital_read(d1) == True:
            break
    
        lcd_hsv(0.02,1,255)
        lcd_clear()
        lcd_print("old button to st")
        sleep(1)
        if digital_read(d1) == True:
            break
    
        lcd_hsv(0.1,1,255)
        lcd_clear()
        lcd_print("ld button to sta")
        sleep(1)
        if digital_read(d1) == True:
            break

        lcd_hsv(0.3,1,255)
        lcd_clear()
        lcd_print("d button to star")
        sleep(1)
        if digital_read(d1) == True:
            break
    
        lcd_hsv(0.62,1,255)
        lcd_clear()
        lcd_print(" button to start")
        sleep(1)
        if digital_read(d1) == True:
            break
        
        lcd_hsv(0.75,1,255)
        lcd_clear()
        lcd_print("button to start.")
        sleep(1)
        if digital_read(d1) == True:
            break
        
    return button

# Function to capture time. time.asctime() is used, but only
# the date and time are returned to print to the LCD.
def timeNow():
    myTime = asctime()
    i = 4
    j = 20
    
    return myTime[i:j]

# Function to display the current temperature for a few seconds.
def tempNow():
    temp = temp_celsius(a1)
    rTemp = round(temp, 2)
    
    lcd_clear()
    lcd_print("It's ")
    lcd_print(rTemp)
    lcd_print(" C")
    sleep(3)
    
# Fun little feature that "Reads minds". Will give a random string
# based on a preset list.
def mindReader():
    while digital_read(d2) == True:
        lcd_clear()
        lcd_print("Reading Mind.")
        sleep(0.5)
        lcd_clear()
        lcd_print("Reading Mind..")
        sleep(0.5)
        lcd_clear()
        lcd_print("Reading Mind...")
        sleep(0.5)
        
        if digital_read(d2) == False:
            lcd_clear()
            lcd_print(random.choice(mind1))
            sleep(1)
            
            lcd_clear()
            lcd_print(random.choice(mind2))
            sleep(1)
            break

# Function to check input
def checkInput(d1, d2):
    val = 0
    if digital_read(d1) == True and digital_read(d2) == False:
        val = d1
    elif digital_read(d1) == False and digital_read(d2) == True:
        val = d2
        
    return val

# Function displaying the gadget after triggered.
# Time is desplayed by default, but different functions are displayed
# depending on which input device is triggered.
def timeDisplay(d1, d2):
    checkInput(d1, d2)
    
    while checkInput(d1, d2) == 0:
        
        lcd_clear()
        lcd_print(timeNow())
        sleep(0.5)
        
        if checkInput(d1, d2) == 2:
            tempNow()
        
        elif checkInput(d1, d2) == 6:
            mindReader()

# Variables
# ---------------------------------------------------------

d1 = 2
d2 = 6
a1 = 0

button = digital_read(d1)
touch = digital_read(d2)

mind1 = [
    "Attracted to",
    "Embarrassed by",
    "Afraid of",
    "In denial of",
    "Enraged by",
    "Puzzled by",
    "Optimistic about",
    "Curious about",
    "Worried about"]

mind2 = [
    "a colleague",
    "your wallet",
    "clowns",
    "old age",
    "new shoes",
    "fashion trends",
    "the past",
    "COVID-19"]

# Project Script
# ---------------------------------------------------------

lcd_clear()
startScreen(d1, button)

lcd_clear()
lcd_print("Hello, World!")        
lcd_rgb(255,255,255)
sleep(1)

timeDisplay(d1, d2)

# Notes
# ---------------------------------------------------------

# time function: time.asctime()
    
# Temperature Sensor:
    # Voltage = 3.3 ~ 5V
    # Zero Power Resistance = 100K(Ohms)
    # Resistance Tolerance = (+-)1%
    # Operating Temperature Range = -40 ~ 125 C
    # Nominal B Constant = 4250 ~ 4299K
        
# print 2 decimal points:
    # x = variable
    # print("%.2f" % x)
    # or round(x, 2)
    
# random element from list: random.choice(list)