  
#Code by: Srushti Shimpi
#Hackerrank Day 9 Challange

#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input())

# Complete the factorial function below.
def factorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))
