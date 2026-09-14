# "Hello World!" in C

## HackerRank

https://www.hackerrank.com/challenges/hello-world-c/problem?isFullScreen=true

## Language

C

## Problem Statement

|
Prepare
Certify
Compete
|
Switch to..
PrepareCIntroduction"Hello World!" in C
"Hello World!" in C
15 more points to get your first star!
Rank: 1441289|Points: 0/15
C language
Problem
Submissions
Leaderboard
Discussions
Editorial
|
PrepareCIntroduction"Hello World!" in C
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial

Objective

In this challenge, we will learn some basic concepts of C that will get you started with the language. You will need to use the same syntax to read input and write output in many C challenges. As you work through these problems, review the code stubs to learn about reading from stdin and writing to stdout.

Task

This challenge requires you to print  on a single line, and then print the already provided input string to stdout. If you are not familiar with C, you may want to read about the printf() command.

Example


The required output is:

Hello, World!  
Life is beautiful  


Function Descriptio

Complete the main() function below.

The main() function has the following input:

string s: a string

Prints

*two strings: * "Hello, World!" on one line and the input string on the next line.

Input Format

There is one line of text, .

Sample Input 0

Welcome to C programming.


Sample Output 0

Hello, World!
Welcome to C programming.

Change Theme
Language: C
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
#include <stdio.h>
int main() {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    printf("Hello, World!\n");
    printf("%s", s);
    return 0;
}
Line: 13 Col: 1
Submit Code
Run Code
Upload Code as File
Test against custom input
BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy

