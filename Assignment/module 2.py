#1
Name = str(input("what is your name?:"))
print("Hello," +(Name))

#2
Circle_rad = float(input("What is the radius of the circle?:"))
answer = 3.14*(Circle_rad**2)
print("The area of the circle is:"+ str(answer))


#3
length = float(input("what is the length?: "))
width = float(input("what is the width?: "))
Per = ((length*2)+(width*2))
Area = (length*width)
print(f"The perimiter is: {Per}" )
print(f"The area is: {Area}")

#4
one = float(input("what is the first integer?: "))
two = float(input("what is the second integer?: "))
three = float(input("what is the third integer?:"))
print(f"The Sum of the integers are {one+two+three}")
print(f"The Product of the integers are {one*two*three}")
print(f"The Average of the integers are {(one+two+three)/3}")


#5
import math
talents = float(input("what is the talent?: "))
pound = float(input("what is the pounds?: "))
lot = float(input("what is the lot?: "))
pound_per_talent = 20
lot_per_pound = 32
grams_per_lot = 13.3

computation_to_lot = ((pound_per_talent*talents+pound)*lot_per_pound+lot)

Kilogram = (computation_to_lot*grams_per_lot)/1000
Gram = Kilogram * 1000%1000

print(f"The units to Kilogram is {math.trunc(Kilogram):3.0f} & \n The units to gram is {Gram:5.2f}")

#6

import random

three_randoms = ''.join([str(random.randint(0, 9)) for _ in range(3)])
print(f"3-digit code: {three_randoms}")

four_randoms =''.join([str(random.randint(1, 6)) for _ in range(4)])
print(f"4-digit code: {four_randoms}")