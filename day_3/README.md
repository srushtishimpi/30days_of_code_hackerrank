# Hackerrank Challenge - Day 3: Intro to Conditional Statements

## Objective
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

## Task
Given an integer, **_n_**, perform the following conditional actions:

* If  is odd, print Weird
* If  is even and in the inclusive range of **2** to **5**, print Not Weird
* If  is even and in the inclusive range of **6** to **20**, print Weird
* If  is even and greater than **20**, print Not Weird

Complete the stub code provided in your editor to print whether or not **_n_** is weird.

## Input Format

A single line containing a positive integer, **_n_**.

* Constraints: <br/>
**_1 <= n <= 100_**

## Output Format

Print **Weird** if the number is weird; otherwise, print **Not Weird**.

### Sample Input 0
```
3
```
### Sample Output 0
```
Weird
```
### Sample Input 1
```
24
```
### Sample Output 1
```
Not Weird
```

## Explanation

### Sample Case 0: 
**_n = 3_** <br/>
**_n_** is odd and odd numbers are weird, so we print **Weird**.

### Sample Case 1: 
**_n = 24_** <br/>
**_n>20_** and **_n_** is even, so it isn't weird. Thus, we print **Not Weird**.
