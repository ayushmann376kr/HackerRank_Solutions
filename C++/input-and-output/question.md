# Input and Output

## HackerRank URL

https://www.hackerrank.com/challenges/cpp-input-and-output/problem?isFullScreen=true

## Category

C++

## Language

Unknown

## Problem Statement

|
Prepare
Certify
Compete
|
Switch to..
PrepareC++IntroductionInput and Output
Input and Output
30 more points to get your next star!
Rank: 1161620|Points: 10/40
CPP
Your Input and Output submission got 5.00 points.  
You are now 30 points away from the 2nd star for your c++ badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
|
PrepareC++IntroductionInput and Output
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial

Objective
In this challenge, we practice reading input from stdin and printing output to stdout.

In C++, you can read a single whitespace-separated token of input using cin, and print output to stdout using cout. For example, let's say we declare the following variables:

string s;
int n;


and we want to use cin to read the input "High 5" from stdin. We can do this with the following code:

cin >> s >> n;


This reads the first word ("High") from stdin and saves it as string , then reads the second word ("") from stdin and saves it as integer . If we want to print these values to stdout, separated by a space, we write the following code:

cout << s << " " << n << endl;


This code prints the contents of string , a single space (), then the integer . We end our line of output with a newline using endl. This results in the following output:

High 5


Task
Read  numbers from stdin and print their sum to stdout.

Input Format

One line that contains  space-separated integers: , , and .

Constraints

Output Format

Print the sum of the three numbers on a single line.

Sample Input

1 2 7


Sample Output

10


Explanation

The sum of the three numbers is .

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
#include <iostream>
using namespace std;
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << a + b + c << endl;
    return 0;
}
Line: 9 Col: 2
Submit Code
Run Code
Upload Code as File
Test against custom input
CPP
You have earned 5.00 points!
You are now 30 points away from the 2nd star for your c++ badge.
0%
10/40
Congratulations
You solved this challenge. Would you like to challenge your friends?
Share on X
Share on LinkedIn
Next Challenge
Test case 0
Test case 1
Test case 2
Test case 3
Test case 4
Test case 5
Compiler Message
Success
Input (stdin)
Download
1 2 7
Expected Output
Download
10
BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy
