# -*- coding: utf-8 -*-
"""
Day identifying algorithm

@author: Nitin
"""
print("This program is to determine the day of the date you enter between 1600 and 2099")
year = [6,4,2,0,6]
month = [0,3,3,6,1,4,6,2,5,0,3,5]

dd = int(input("Enter the date (DD): " ))
mn = int(input("Enter the month(MM): "))
yr = input("Enter the year(YYYY): ")
y = int(yr[-2:])
s1 = dd +  y
s2 = y//4
s3 = s1+s2
s3 += month[mn-1]
if int(yr) in range(1600,2100):
    if(int(yr) in range(1600,1700)):
        s3 += year[0];
    elif(int(yr) in range(1700-1800)):
        s3 += year[1]
    elif(int(yr) in range(1700,1800)):
        s3+=year[2]
    elif(int(yr) in range(1800,1900)):
        s3+=year[3]
    elif(int(yr) in range(1900,2000)):
        s3+=year[4]
    elif(int(yr) in range(2000,2100)):
        s3+=year[5]
        
    s4 = s3%7
    if s4==0:                       #This part of code can be simplified by using two lists
        print("It was Sunday")
    elif s4==1:
        print("It was Monday")
    elif s4==2:
        print("It was Tuesday")
    elif s4 ==3:
        print("It was Wednesday")
    elif s4 == 4:
        print("It was thursday")
    elif s4 == 5:
        print("It was Friday")
    elif s4 == 6:
        print("It was Saturday")
    else:
        print("Program Error")
else:
    print("The year you've entered is invalid for this program")
    

