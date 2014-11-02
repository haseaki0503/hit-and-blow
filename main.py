#coding: utf-8
import random

Answer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def Initialization():
	for x in range(1,1000):
	  j = random.randint(0,9)
	  k = random.randint(0,9)
	  tmp = Answer[j]
	  Answer[j] = Answer[k]
	  Answer[k] = tmp

#MAIN
Initialization()

for x in range(0,9):
  print(Answer[x])

GuessInput = input("Guess===>")
