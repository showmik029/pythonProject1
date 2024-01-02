#task1
import random
def random_dice():
  return random.randint(1,6)
def main_program():
 while True:
  x=random_dice()
  print(x)
  if x==6:
   break
main_program()

#task2
import random
n=int(input('enter a number'))
def random_dice(k):
  return random.randint(1,n)
random_dice(n)
print(f"hi dan {random_dice(n)}")

def main_program():
 while True:
  x=random_dice(n)
  print(x)
  if x==n:
   break
main_program()

#task3
def gasoline(gas):
  liter=gas*3.7689
  return liter
def main_function():
  while True:
   inp=int(input())
   ans=gasoline(inp)
   if inp<0:
    print('wrong number dan :)')
    break
   else:
    print(ans)
main_function()

#task4
def function(x):
  num=0
  for i in x:
    num+=int(i)
  return num

print(function([1,2,3,4,5]))

#task5
def function(x):
  lst1=[]
  for i in x:
   i=int(i)
   if i%2==0:
    lst1.append(i)
  return lst1
x=[1,2,3,4,5]
print(x)
print(function(x))

#task6
import math
def calculator1(dia,pri):
 area=math.pi*(dia/2)**2
 sqm=area/10000
 perunit=pri/sqm
 return perunit
def main_function():
  dia=float(input('enter the diameter' ))
  pri=(float(input('enter the price ')))
  x=calculator1(dia,pri)
  dia2=float(input('enter the diameter of second pizza' ))
  pri2=(float(input('enter the price pf the second pizza ')))
  y=calculator1(dia2,pri2)
  if x<y:
    print("first pizza is value for money")
  elif x==0:
    print("they are the same bro just go for the one your heart desires")
  else:
    print("please just go for the second pizza")
main_function()
