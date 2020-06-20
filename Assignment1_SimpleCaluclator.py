# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:25:11 2020

@author: vishal
"""
#Simple Caluclator

print("Please select operation -\n" 
        "1. Add\n"  
        "2. Subtract\n"  
        "3. Multiply\n"  
        "4. Divide\n"
        "5. MOdulus\n"
        "6. Exponential\n"
        "7. Double Division\n")
  
  
# Take input from the user  
select = int(input("Select operations no.")) 
  
a= int(input("Enter first number: ")) 
b= int(input("Enter second number: ")) 
  
if select == 1: 
    print("Add=",a+b)
  
elif select == 2: 
    print("sub=",a-b)
  
elif select == 3: 
     print("Mul=",a*b)
elif select == 4:
    print("Div=",a/b)
elif select == 5:
    print("mod=",a%b)
elif select == 6:
    print("exp=",a**b)
elif select == 7:
    print("Double Div=",a//b)
else:
    print("no operation is selected")
                  
                 