#include <stdio.h>

int main() {
    char name[100];

    printf("Enter your name: ");
    scanf("%99s", name);

    printf("Hello, %s! Nice to meet you.\n", name);

    return 0;
}