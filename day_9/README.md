# Hackerrank Challenge - Day 9: Recursion 3
## Objective
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

## Recursive Method for Calculating Factorial
## Task
Write a factorial function that takes a positive integer, **_N_** as a parameter and prints the result of **_N!_** (**_N_** factorial).

**Note**: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of **_0_**.

## Input Format

A single integer, **_N_** (the argument to pass to factorial).

## Constraints
* **_2 <= N <= 12_**
* Your submission must contain a recursive function named factorial.
## Output Format

Print a single integer denoting **_N!_**.

### Sample Input
```
3
```
### Sample Output
```
6
```
##  Explanation

Consider the following steps:
1. **_factorial(3) = 3 X factorial(2)_**
2. **_factorial(2) = 2 X factorial(1)_**
3. **_factorial(1) = 1_**. 

From steps **_2_** and **_3_**, we can say **_factorial(2) = 2 X 1 = 2_**; then when we apply the value from **_factorial(2)_** to step **_1_**, we get **_factorial(3) = 3 X 2 X 1 = 6_**. Thus, we print **_6_** as our answer.
