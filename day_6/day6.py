#Code by: Srushti Shimpi
#Hackerrank Day 6 Challange

#!/bin/python3


import math
import os
import random
import re
import sys

t =int(input()) #task number
for x in range(t):
    string = input() #reading string
    print(string[::2], string[1::2]) #printing even-odd indexe values from input string
