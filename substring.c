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
    
    for (i=0; i < len; i++) {
        for (j=i+1; j < len; j++) {
            if (visited[string[j]] == 1) {
                break;
            } else {
                res = MAX(res, j - i);
                visited[string[j]] = 1;
            }
        }
        visited[string[i]] = 0;
    }
    return res;
}

int main() {
    char input[] = "geeksforgeeks";
    
    printf("%d", substrings(input));
    return 0;
}
