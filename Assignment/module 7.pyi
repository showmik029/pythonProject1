#task1
weather=("winter","spring","summer","autum")
inp=int(input('enter a number of a month: '))
if 0<inp<=12:
  if 3<=inp<=5:
    print(weather[1])
  elif 6<=inp<=8:
    print(weather[2])
  elif 9<=inp<=11:
    print(weather[3])
  else:
    print(weather[0])
else:
  print("invalid num")

#task2
set1=set()
while True:
  inp=input("enter name: ")
  if inp!="":
    if inp in set1:
      print("Existing name")
    elif inp not in set1:
      print("New name")
      set1.add(inp)
  elif inp=="":
    break
for i in set1:
  print(i)
