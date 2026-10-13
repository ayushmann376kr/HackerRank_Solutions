# Basic Data Types

## HackerRank URL

https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem?isFullScreen=true

## Category

C++

## Language

C

## Problem Statement

|
Prepare
Certify
Compete
|
Switch to..
PrepareC++IntroductionBasic Data Types
Basic Data Types
20 more points to get your next star!
Rank: 991533|Points: 20/40
CPP
Your Basic Data Types submission got 10.00 points.  
You are now 20 points away from the 2nd star for your c++ badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
|
PrepareC++IntroductionBasic Data Types
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial

Some C++ data types, their format specifiers, and their most common bit widths are as follows:

Int ("%d"): 32 Bit integer
Long ("%ld"): 64 bit integer
Char ("%c"): Character type
Float ("%f"): 32 bit real value
Double ("%lf"): 64 bit real value

Reading
To read a data type, use the following syntax:

scanf("`format_specifier`", &val)


For example, to read a character followed by a double:

char ch;
double d;
scanf("%c %lf", &ch, &d);


For the moment, we can ignore the spacing between format specifiers.

Printing
To print a data type, use the following syntax:

printf("`format_specifier`", val)


For example, to print a character followed by a double:

char ch = 'd';
double d = 234.432;
printf("%c %lf", ch, d);


Note: You can also use cin and cout instead of scanf and printf; however, if you are taking a million numbers as input and printing a million lines, it is faster to use scanf and printf.

Input Format

Input consists of the following space-separated values: int, long, char, float, and double, respectively.

Output Format

Print each element on a new line in the same order it was received as input. Note that the floating point value should be correct up to 3 decimal places and the double to 9 decimal places.

Sample Input

3 12345678912345 a 334.23 14049.30493


Sample Output

3
12345678912345
a
334.230
14049.304930000


Explanation

Print int ,
followed by long ,
followed by char ,
followed by float ,
followed by double .

Change Theme
Language
C++11
More
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
#include <iostream>
#include <cstdio>
using namespace std;
int main() {
    int i;
    long l;
    char c;
    float f;
    double d;
    scanf("%d %ld %c %f %lf", &i, &l, &c, &f, &d);
    printf("%d\n", i);
    printf("%ld\n", l);
    printf("%c\n", c);
    printf("%.3f\n", f);
    printf("%.9lf\n", d);
    return 0;
}
Line: 21 Col: 2
Submit Code
Run Code
Upload Code as File
Test against custom input
CPP
You have earned 10.00 points!
You are now 20 points away from the 2nd star for your c++ badge.
33%
20/40
Congratulations
You solved this challenge. Would you like to challenge your friends?
Share on X
Share on LinkedIn
Next Challenge
Test case 0
Test case 1
Test case 2
Test case 3
Compiler Message
Success
Input (stdin)
Download
3 12345678912345 a 334.23 14049.30493
Expected Output
Download
3
12345678912345
a
334.230
14049.304930000
BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy
