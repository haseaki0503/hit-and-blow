#coding: utf-8
import random

Answer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
i = 0

def Initialization():
  for x in range(1,1000):
    j = random.randint(0,9)
    k = random.randint(0,9)
    tmp = Answer[j]
    Answer[j] = Answer[k]
    Answer[k] = tmp

def InputCheck(GuessInput):
  if len(GuessInput) != 4:
    print("Error!!")
  else:
    global i
    i += 1
    AnswerCheck(GuessInput)

def AnswerCheck(GuessInput):
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
print("Hit and Blow GAME!!")
Initialization()

while (1):
  GuessInput = input("Guess===>")
  InputCheck(GuessInput)

  if hit == 4:
    print("Congratulations! You're WON!! ")
    break
  if i == 10:
    print("You're LOST...Answer is " + str(Answer[0])+str(Answer[1])+str(Answer[2])+str(Answer[3]))
    break
