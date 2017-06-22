#!/usr/bin/python3
# -*- coding: utf-8 -*-

##### Modules #####

# System (for KeyboardInterrupt)
from sys import exit

# Database
from utils.m_bdd import *

# Show pulse (for lighting indicator when the data is gone to the BDD using the Pimoroni's Blinkt! .)
from utils.m_blinkt_pulse import *

# Time and date
from time import sleep
from datetime import datetime

# Enviro pHAT
from envirophat import light, weather

## Colors
#from utils.m_color_list import *

##### Variables #####

equartT = 7 # Temperature difference when Enviro is on the up position in °C
interval = 900 # ms

# ---->

##### Functions #####
def harvest():
	
	date = datetime.now()
	
	##### Grab Sense Hat data #####
	
	t = round((weather.temperature()- equartT), 1)
	p = round((weather.pressure() / 100), 1)
	l = light.light()

	##### MySQL sign in #####
	conn = pymysql.connect(user="user",passwd="userpassWD",host="192.168.x.x",database="sensors")
	cursor = conn.cursor()

	##### Database insertion #####
	##### Global cursor ####
	cursor.execute(queryInsert("temperature", t, "Enviro pHAT", "room 1"))
	cursor.execute(queryInsert("pression", p, "Enviro pHAT", "room 1"))
	cursor.execute(queryInsert("light", l, "Enviro pHAT", "room 1"))

	##### Disconnect the database #####
	conn.commit()
	cursor.close()
	conn.close()

# 	print(date,' Temperature : ',t,'. Pression : ',p,'. Lumière : ',l)

##### Program #####
try:
	
	#### Setting up the LEDs brightness
	#set_brightness(0.1)
	
	while 1:
		## Used a try to prevent the crash of the script if the database not contactable
		try:
			blinkt_pulse('blue') # Just to have a visual feedback on the Blinkt!
			#### Pick up the data
			harvest()
			
			#### Wait a while
			sleep(interval)
		except Exception:
			print("harvest() function had a problem.")
			sleep(10)
			pass
		

##### End #####
except KeyboardInterrupt:
	blinkt_pulse('red')
	exit()
