# Hackerrank Challenge - Day 6: Let's review (String + Loop)

## Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

## Task
Given a string, **_S_**, of length **_N_** that is indexed from **_0_** to **_N_**, print its even-indexed and odd-indexed characters as **2** space-separated strings on a single line (see the Sample below for more detail).

**Note: 0 is considered to be an even index.**

## Input Format

The first line contains an integer, **_T_** (the number of test cases).
Each line **_i_** of the **_T_** subsequent lines contain a String, **_S_**.


## Constraints
* **_1 <= T <= 10_**
* **_2 <= length of S <= 10000_**

## Output Format

For each String **_Sj_** (where **_0 <= j <= T-1_**), print **_Sj_**'s even-indexed characters, followed by a space, followed by **_Sj_**'s odd-indexed characters.

### Sample Input
```
2
Hacker
Rank
```
### Sample Output
```
Hce akr
Rn ak
```
## Explanation

### Test Case 0: 
**S = "Hacker"** <br/>
**S[0] = "H"** <br/>
**S[1] = "a"** <br/>
**S[2] = "c"** <br/>
**S[3] = "k"** <br/>
**S[4] = "e"** <br/>
**S[5] = "r"** <br/>

The even indices are **0**, **2**, and **4**, and the odd indices are **1**, **3**, and **5**. We then print a single line of **2** space-separated strings; the first string contains the ordered characters from **_S_**'s even indices (**Hce**), and the second string contains the ordered characters from **_S_**'s odd indices (**akr**).

### Test Case 1: 
**S = "Rank"** <br/>
**S[0] = "R"** <br/>
**S[1] = "a"** <br/>
**S[2] = "n"** <br/>
**S[3] = "k"** <br/>



The even indices are **0** and **2**, and the odd indices are **1** and **3**. We then print a single line of **2** space-separated strings; the first string contains the ordered characters from **_S_**'s even indices (**Rn**), and the second string contains the ordered characters from **_S_**'s odd indices (**ak**).
