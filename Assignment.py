# write a program to calculate the area of reactange
height = float(input("Enter height of Rectangle:"))
width = float(input("Enter width of Rectangle:"))
area_Of_Rectangle = width * height
print(area_Of_Rectangle)

# write a program to calcuate Area of Square
s = float(input("Enter side of square"))
area = s*s
print(area)

# write a program to prime number or not
num = 7
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int(pow(num,0.5)+1)):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")