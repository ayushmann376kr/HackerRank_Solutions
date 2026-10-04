
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