import random

def check (comp,user):
  if comp == user:
    return 0
  if (comp ==0 & user==-1):
    return -1
  if (comp ==1 & user==2):
    return -1
  if (comp ==2 & user==0):
    return -1
  return 1

comp = random.randint(0,2)
user = int (input("0 for snake, 1 for water and 2 for gun\n"))

score = check(comp,user)
print("you:",user)
print("computer:",comp)

if(score ==0):
  print("It's a draw")

elif(score ==-1):
  print("you loose")

else:
  print("you win")

  