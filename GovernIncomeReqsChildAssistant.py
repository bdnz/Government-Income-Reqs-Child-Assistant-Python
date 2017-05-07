#!/usr/bin/python3

import math
import sys

#income = int(input("What is the HouseHold income? "))
# print (income)

#child = int(input("How many children? "))
# print (child)


counter = 1
while (counter < 100):

 income = int(input("What is the HouseHold income? "))
# print (income)

 child = int(input("How many children? "))
# print (child)

 if (30000 <= income < 40000) and (child >= 3) :

   print("----------")
   print ("The Assisntance Amount is: $", child * 1000)

 if (30000 <= income < 40000) and (child < 3) :

   print("----------")
   print ("The Assistance Amount is: $0.00.")

 if (20000 <= income < 30000) and (child >= 2) :

   print("----------")
   print ("The Assisntance Amount is: $", child * 1500)

 if (20000 <= income < 30000) and (child < 2) :

   print("----------")
   print ("The Assistance amount is: $0.00")

 if (0 <= income < 20000 ) :

   print("----------")
   print ("The Assistance Amount is: $", child * 2000)

 if (income > 40000) and (child >= 0) :

  print("----------")
  print ("You don't meet the req to receive government benefits.   Asis. Amount: $0.00")


counter += 1

#print (counter)
