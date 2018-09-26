#_*_ coding:utf8-

#1
'''
import math
r = float(raw_input("Enter the length from the center to a vertex:"))
s = 2 * r * math.sin(math.pi/5)
Area = 5 * s * s /(4 * math.tan(math.pi/5))
print('The area of the pentagon is %0.2f' %Area)
'''
#2
import math
x1,y1 = eval(raw_input("Enter point 1(latitude and longitude) in degrees:"))
x2,y2 = eval(raw_input("Enter point 2(latitude and longitude) in degrees:"))
r = 6371.01
d = radius*math.arccos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+math.cos(math,radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1)-math.radians(y2))
print('The distance between the two points is {} km'.format(d))
#3
'''
import math
s = float(raw_input("Enter the side:"))
Area = (5 * s * s)/(4 * math.tan(math.pi/5))
print('The area of the pentagon is {}'.format(Area))
'''
#4
'''
import math
n = float(raw_input("Enter the number of sides:"))
s = float(raw_input("Enter the side:"))
Area = (n*s*s)/(4*math.tan(math.pi/n))
print('The area of the polygon is {}'.format(Area))
'''
#5
'''
import math
number = int(raw_input("Enter an ASCII code:"))
print('The character is {}'.format(chr(number)))
'''
#6
'''
name = (raw_input("Enter employee's name:"))
time = float(raw_input("Enter number of hours worked in a week:"))
h = float(raw_input("Enter hourly pay rate:"))
f = float(raw_input("Enter federal tax withholding rate:"))
s = float(raw_input("Enter state tax withholding rate:"))
Gross = time * h
print('Employee Name: {}'.format(name))
print('Hours Worked: {}'.format(time))
print('Pay rate: {}'.format(h))
print('Gross Pay: {}'.format(Gross))
Federal = Gross * f
State = Gross * s
Total = Federal + State
Pay = Gross - Total
print('Deductions:')
print('  FederalWithholding (20.0%): {}'.format(Federal))
print('  State Withholding(9.0%): {}'.format(State))
print('  Total Deduction: {}'.format(Total))
print('Net Pay: {}'.format(Pay))
'''
