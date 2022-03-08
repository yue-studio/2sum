//
// based on https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
//
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX(a,b)            (((a) > (b)) ? (a) : (b))

int substrings(char *string) {
    int i,j;
    int len = strlen(string);
    int res = 0;
    int visited[256];
    
    for (i = 0; i < len; i++) {
        for (j = i; j < len; j++) {
            printf("%d %d checking %c \n ", i,j,string[j]);
            if (visited[string[j]] == 1) {
                printf("visited\n");
                printf(" break\n");
                break;
            } else {
                res = MAX(res, j - i + 1);
                visited[string[j]] = 1;
                printf("unique, set visited %c to 1, length: %d\n", string[j], res);
            }
        }
        visited[string[i]] = 0;
        printf("clearing %c\n", string[i]);
    }
    return res;
}

int main() {
    char input[] = "geeksforgeeks";
    
    printf("%d", substrings(input));
    return 0;
}
