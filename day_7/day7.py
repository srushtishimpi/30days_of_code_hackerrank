  
#Code by: Srushti Shimpi
#Hackerrank Day 7 Challange

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    reverse_a = a[::-1]
    print(*reverse_a) # * operator help to print list without brackert and with spaces in between

