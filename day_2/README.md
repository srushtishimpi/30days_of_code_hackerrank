# Hackerrank Challenge - Day 2: Operators

## Objective
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

## Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

**Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!**

## Input Format

There are 3 lines of numeric input:<br/>
The first line has a double, **_mealCost_** (the cost of the meal before tax and tip).<br/>
The second line has an integer, **_tipPercent_** (the percentage of **_mealCost_** being added as tip).<br/>
The third line has an integer, **_taxPercent_** (the percentage of **_mealCost_** being added as tax).

## Output Format

Print the total meal cost, where **_totalCost_** is the rounded integer result of the entire bill (**_mealCost_** with added tax and tip).

### Sample Input
```
12.00
20
8
```
### Sample Output
```
15
```
## Explanation

Given:<br/>
**_mealCost_ = 12, _tipPercent_ = 20, _taxPercent_ = 8**

Calculations:<br/>
**_tip_ = (12 X 20)/100 = 2.4**<br/>
**_tax_ = (12 X 8)/100 = 0.96**<br/>
**_totalCost_ = _mealCost_ + _tip_ +_tax_ = 12 + 2.4 + 0.96 = 15.36**<br/>
**_round_(_totalCost_) = 15**

We round **_totalCost_** to the nearest dollar (integer) and then print our result, **15**.
