#Code by: Srushti Shimpi
#Hackerrank Day 10 Challange


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input()) #Reading input integer.
    binary_num = str("{0:b}".format(n)).split('0') #Converting interger to binary and splitting binary number with '0'.
    #print(binary_num)

    l = [len(i) for i in binary_num] #Counting the length of all the strings splitted by '0'.
    
print(max(l)) #Printing maximum length.
