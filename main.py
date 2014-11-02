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

def AnswerCheck():
        global hit
        global blow

        hit=0
        blow=0
        
        for x in range(0, 4):
                if Answer[x] == GuessInput[x]:
                        hit += 1

        for x in range(0, 4):
          for y in range(0, 4):
            if Answer[x] == GuessInput[y]:
              blow += 1
              break
        blow -= hit
        print("hit= " + str(hit) + " " + "blow= " + str(blow))
        
#MAIN
Initialization()

for f in range(0, 9):
	GuessInput = input("Guess===>")
	AnswerCheck()

  if hit == 4:
		print("Congratulations!!")
		break

print("Answer= " + str(Answer[0])+str(Answer[1])+str(Answer[2])+str(Answer[3]))
