

# Function that handles fighting
  #Announce what's fighting what, do some basic description
  #Asks user for input
  #Ask which Nomi to send out first
  #Ask them which move they want to use
  #Resolution order: Priority, speed, etc.
  #Idea: Alternate these questions and prompt players 1 and 2 for what they want to do
  #resolve damage, run damage calculation formulas, compare attks and defs, check moods, etc.
  #Check if one of our combatants has been eliminated(Next round)
  #also want to be checking at the end of each round if the battle is over or surrender

import random
from nomi import *

playerHP = 0
enemy = 0

def attack(myNomi, enemyNomi, enemyMove):
  prompt = True
  while prompt:
    print("Available moves: \n")
    i = 1
    for move in myNomi.moveSet:
      print("{}: {}".format(i, myNomi.moveSet[i]))
      i += 1
    action = input("Choose a move number: ")

    if action == 1:
      myMove = myNomi.moveSet[0]
    elif action == 2:
      myMove = myNomi.moveSet[1]
    elif action == 3:
      myMove = myNomi.moveSet[2]
    elif action == 4:
      myMove = myNomi.moveSet[3]
    else:
      print("Invalid input")

  #Calculating who goes first - checking priority and all that jazz
  if myMove.priority > enemyMove.priority:
    enemyNomi.calculateDamage(myMove, myNomi.attack)
    if enemyNomi.hp != 0:
      myNomi.calculateDamage(enemyMove, enemyNomi.attack)

  elif myMove.priority < enemyMove.priority:
    myNomi.calculateDamage(enemyMove, enemyNomi.attack)
    if enemyNomi.hp != 0:
      myNomi.calculateDamage(enemyMove, enemyNomi.attack)
  
  elif myMove.priority == enemyMove.priority:
    if myNomi.att_speed > enemyNomi.att_speed:
      enemyNomi.calculateDamage(myMove, myNomi.attack)
      if enemyNomi.hp != 0:
        myNomi.calculateDamage(enemyMove, enemyNomi.attack)
    
    elif myNomi.att_speed < enemyNomi.att_speed:
      myNomi.calculateDamage(enemyMove, enemyNomi.attack)
      if enemyNomi.hp != 0:
        myNomi.calculateDamage(enemyMove, enemyNomi.attack)
    
    #if both priority and speed are the same, throw a coin to determine who goes first
    
    elif myNomi.att_speed == enemyNomi.att_speed:
      toss = random.randint(1,2)
      
      if toss == 1:
        enemyNomi.calculateDamage(myMove, myNomi.attack)
        if enemyNomi.hp != 0:
          myNomi.calculateDamage(enemyMove, enemyNomi.attack)
      else:
        myNomi.calculateDamage(enemyMove, enemyNomi.attack)

