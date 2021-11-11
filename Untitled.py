import json
import discord
import random
import time
from MafiaClass import Player
from MafiaCommands import StartRules, Start 

NumPlayers = 0
RoleList = ['Citizen', 'Mafia', 'Doctor', 'Sheriff']

def RoleClaim():
	print ('hey peeps')

def sleep():
	time.sleep(1)

def Night(TestList):
	print("It is now night time, everyone mute their mics")
	sleep()
	Saved = input ("Doctor, please @ who you would like to save")
	x = 0
	for players in TestList:
		if TestList[x] == Saved:
			TestList[x]
	sleep()
	

p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()
p5 = Player()
p6 = Player()
p7 = Player()
p8 = Player()
p9 = Player()
p10 = Player()

TestList = [p1,p2,p3,p4,p5,p6]

x=0
for players in TestList:
	print(TestList[x].role)

Start()