#include <stdio.h>
int* twoSum(int* nums, int numsSize, int target){
     static int out[2];
     int i,j;
     
     for (i=0;i< numsSize; i++) {
         for (j=i+1; j< numsSize;j++) {
             if (nums[i] + nums[j] == target) {
                 out[0] = i;
                 out[1] = j;
             }
         }
     }
     
     return out;
}

int* twoSumHash(int* nums, int numsSize, int target){
    static int out[2];
    int i, temp;
 
    /*initialize hash set as 0*/
    int s[1000] = { 0 };
 
    for (i = 0; i < numsSize; i++)
    {
        temp = target - nums[i];
        if (s[temp] == 1) {
//            printf("Pair with given sum %d is (%d, %d) \n", target, nums[i], temp);
                out[0] = nums[i];
                out[1] = temp;
        }
        s[nums[i]] = 1;
    }
    return out;
}


int main() {
    int nums[] = {2, 7, 11, 15};
    int size = sizeof(nums) / sizeof(nums[0]);
    int *output;
    int i;
    
    output = twoSumHash(nums, size, 9);
    for (i=0; i< 2; i++) {
        printf("%d ", output[i]);
    }
    
    return 0;
}
