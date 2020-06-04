# Write your code here
import random

# Intro (get name, say hello)
name=input("Enter your name: ")
print("Hello, "+ name)

#def rotate function
def rotate(l, n):
  return l[n:] + l[:n]

score = 0
# Match username to text file
rating = open('rating.txt','r+')
for line in rating:
  line = line.split()
  if name == line[0]:
    score = int(line[1])
  else:
   filler = 0
#define choices and find middle index
user_choice = None
same_index = None
choices =input()
if choices == "":
    choices ="rock,paper,scissors"
choices = choices.split(",")
mid_index = int((len(choices)+1)/2)
mid = mid_index+1

#FIND INDEX MATCHING USER CHOICE
def match_index(bank,u_choice):
    global same_index
    count = -1
    for i in bank:
      count +=1
      if i == u_choice:
        same_index = count

print()
print("Okay, let's start")

while user_choice != "!exit":
    user_choice = input()
    opp_choice = choices[random.randint(0,len(choices)-1)]
    if user_choice == "!exit":
        print("Bye!")
    elif user_choice == "!rating":
        print("Your rating: "+ str(score))
    elif user_choice in choices:
      match_index(choices,user_choice)
      num = int(same_index - (mid_index-1))
      choices_2 = rotate(choices,num)
      # choice beat options
      b1 = mid_index-1
      b2 = mid_index
      beat = choices_2[0:b1]
      lose = choices_2[b2:99]
        # Draw Condition
      if user_choice == opp_choice:
          option = user_choice
          score += 50
          print("There is a draw (" + user_choice+")")

      elif opp_choice in beat:
            print("Well done. Computer chose "+opp_choice+ " and failed")
            score += 100

      elif opp_choice in lose:
            print("Sorry, but computer chose "+opp_choice)
    else:
        print("Invalid input")
