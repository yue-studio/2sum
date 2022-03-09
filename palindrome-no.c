// from https://www.programiz.com/c-programming/examples/palindrome-number
#include <stdio.h>

int main() {
  int n, reversed = 0, remainder, original;
    printf("Enter an integer: ");
    scanf("%d", &n);
    original = n;

    // reversed integer is stored in reversed variable
    while (n != 0) {
        printf("n %d\n", n);
        remainder = n % 10;
        printf("...remainder %d\n", remainder);
        reversed = reversed * 10 + remainder;
        printf("...reversed %d\n", reversed);
        n /= 10;
    }

    // palindrome if orignal and reversed are equal
    if (original == reversed)
        printf("%d is a palindrome.", original);
    else
        printf("%d is not a palindrome.", original);

    return 0;
}
