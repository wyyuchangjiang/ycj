#1
'''
celsius = float(raw_input("Enter a degree in Celsius:")) 
fahrenheit = ((9.0 / 5.0) * celsius + 32)
print('%0.1f Celsius is %0.1f Fahrenheit ' %(celsius,fahrenheit))
'''
#2
'''
radius,length = eval(raw_input("Enter the radius and length of a cylinder:"))
area = radius * radius * 3.1415
volume = area * length
print('The area is {}'.format(area))
print('The volume is {}'.format(volume))
'''
#3
'''
feet = float(raw_input("Enter a value for feet:"))
meters  = feet * 0.3048
print('{} feet is {} meters'.format(feet,meters))
'''
#4
'''
M = float(raw_input("Enter the amount of water in kilogams:"))
initialTemperature = float(raw_input("Enter the initial temperature:"))
finalTemperature = float(raw_input("Enter the final temperature:"))
Q = M * (finalTemperature - initialTemperature) * 4184
print('The energy needed is{}'.format(Q))
'''
#5
'''
b,i = eval(raw_input("Enter balance and interest rate(e.g., 3 for 3%):"))
c = b * (i/1200)
print('The interest is {}'.format(c))
'''
#6
'''
v0,v1,t = eval(raw_input("Enter v0, v1 and t:"))
a = (v1 - v0)/t
print('The average acceleration is {}'.format(a))
'''
#7
'''
mon = float(raw_input("Enter the monthly saving amount:"))
a = 0.05/12
q = 1+a
b = mon*q
c = (mon + b)*q
d = (mon + c)*q
e = (mon + d)*q
f = (mon + e)*q
g = (mon + f)*q
print('After the sixth month, the account value is {}'.format(g))
'''
#8
a = int(raw_input("Enter a number between 0 and 1000:"))
x = a%10
b = a/10
y = b%10
z = b/10
sum = x+y+z
print('The sum of the digits is {}'.format(sum))
