  
#Code by: Srushti Shimpi
#Hackerrank Day 6 Challange

import math
import os
import random
import re
import sys
import string
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phonebook = {}

for i in range(n): 
    l = input() #Reading first n inputs
    x, y = l.split() #Splitting strings wrt whitespace and saving names in x and numbers in y variable
    phonebook[x]= y  #Saving phone numbers string in phonebook wrt names
    
while True:
    try:
        ph_name = input() #Reading last n string inputs
    except EOFError: #EOFError handling
         break
    if ph_name not in phonebook: #checking if given input is match with any entries in phonebook
        print("Not found")
    else:
        print(ph_name+"="+phonebook[ph_name])

