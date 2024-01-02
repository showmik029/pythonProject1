#1
howmany=int(input())
sum=0
for i in range(1,howmany+1):
  sum+=i
print(sum)

#task2
lst1 = []
inp2=[]
while True:
    inp = input()
    if inp == "":
        break
    else:
        inp= int(inp)
        lst1.append(inp)

lst1.sort()
lst1.reverse()
print(lst1)

#task3
inp=int(input())
count=0
for i in range(1,inp+1):
  if inp%i==0:
    count+=1
if count>2:
      print("Not a prime Number")
else:
      print('Prime Number')

#task4
lst1=[]
for i in range(0,5):
  inp=input("enter the city name: ")
  lst1.append(inp)
for i in lst1:
  print(i)


