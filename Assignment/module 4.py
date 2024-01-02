#1
number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#task2
while True:
 inches=int(input())
 if inches<0:
  break
 else:
  x=inches*2.54
  print(x)
#task3
lst1=[]
while True:
  inp=input()
  if inp!='':
    lst1.append(inp)
  else:
    break
x=max(lst1)
y=min(lst1)
print('Max',x)
print('Min',y)

#4
import random
x=random.randint(1,10)
print(x)
while True:
 y=int(input("please press a number "))
 if x==y:
  print("correct")
  break
 elif x>y:
  print("Too low ")
 else:
   print('Too high')

#task5
username='python'
password='rules'

count=12
while True:
  userip=input('Please Enter the username: ')
  userpw=input('Please Enter the password: ')
  if username==userip and password==userpw:
    print("welcome")
    break
  elif (username!=userip or password!=userpw) and count<5:
    print("please enter the username and the password again ")
    count+=1
  elif count==5:
    print("Access Denied")
    break
