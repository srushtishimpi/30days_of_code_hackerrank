#Code by: Srushti Shimpi
#Hackerrank Day 3 Challange

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    if((n%2)!= 0 ):
        print('Weird')

    elif((n%2)==0 and ((2<=n<=5) or (n>20))):
        print('Not Weird')

    elif((n%2)==0 and (6<=n<=20)):
        print('Weird')


    
