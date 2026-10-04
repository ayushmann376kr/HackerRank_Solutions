# Playing With Characters

## HackerRank

https://www.hackerrank.com/challenges/playing-with-characters/problem?isFullScreen=true

## Language

C

## Problem Statement

|
Prepare
Certify
Compete
|
Switch to..
PrepareCIntroductionPlaying With Characters
Playing With Characters
10 more points to get your first star!
Rank: 1182406|Points: 5/15
C language
Your Playing With Characters submission got 5.00 points.  
You are now 10 points away from the 1st star for your c badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
|
PrepareCIntroductionPlaying With Characters
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial

Objective

This challenge will help you to learn how to take a character, a string and a sentence as input in C.

To take a single character  as input, you can use scanf("%c", &ch ); and printf("%c", ch) writes a character specified by the argument char to stdout

char ch;
scanf("%c", &ch);
printf("%c", ch);


This piece of code prints the character .

You can take a string as input in C using scanf(“%s”, s). But, it accepts string only until it finds the first space.

In order to take a line as input, you can use scanf("%[^\n]%*c", s); where  is defined as char s[MAX_LEN] where  is the maximum size of . Here, [] is the scanset character. ^\n stands for taking input until a newline isn't encountered. Then, with this %*c, it reads the newline character and here, the used * indicates that this newline character is discarded.

Note: The statement: scanf("%[^\n]%*c", s); will not work because the last statement will read a newline character, \n, from the previous line. This can be handled in a variety of ways. One way is to use scanf("\n"); before the last statement.

Task

You have to print the character, , in the first line. Then print  in next line. In the last line print the sentence, .

Input Format

First, take a character,  as input.
Then take the string,  as input.
Lastly, take the sentence  as input.

Constraints

Strings for  and  will have fewer than 100 characters, including the newline.

Output Format

Print three lines of output. The first line prints the character, .
The second line prints the string, .
The third line prints the sentence, .

Sample Input 0

C
Language
Welcome To C!!


Sample Output 0

C
Language
Welcome To C!!

Change Theme
Language: C
More
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
22
23
24
25
1
int main() {
    char ch;
    char s[100];
    char sentence[100];
    // Take character input
    scanf("%c", &ch);
    // Take string input
    scanf("%s", s);
    // Remove newline left by previous input
    scanf("\n");
    // Take sentence input
    scanf("%[^\n]%*c", sentence);
    // Print output
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sentence);
    return 0;
#include <stdio.h>
Line: 26 Col: 2
Submit Code
Run Code
Upload Code as File
Test against custom input
C language
You have earned 5.00 points!
You are now 10 points away from the 1st star for your c badge.
33%
5/15
Congratulations
You solved this challenge. Would you like to challenge your friends?
Share on X
Share on LinkedIn
Next Challenge
Test case 0
Test case 1
Test case 2
Compiler Message
Success
Input (stdin)
Download
C
Language
Welcome To C!!
Expected Output
Download
C
Language
Welcome To C!!
BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy

