import random
print("this is a guess the number game!")
number = random.randint(0,100)
count = 0
while True:
 num1 = int(input("please enter a guessed number between 0 and 100: "))
 if num1 ==number:
  print("you have successfully guesed the correct number")
  break
 else:
  if num1<number:
   print("you have entered a low number")
  elif num1>number:
   print("you have entered a number greater than the random number")
  count+=1
  if count==5:
   print("you have reached the maximum number of trials")
   option = input("Do you still want to continue (yes) (no): ")
   if option =='yes':
    continue
   elif option == 'no':
    break
  elif count<5:
   continue
