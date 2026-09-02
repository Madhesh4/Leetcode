#include <stdbool.h>
#include <string.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int maxDiff(int* nums, int i, int j, int memo[20][20]) {
    if (i == j) {
        return nums[i];
    }
    
    if (memo[i][j] != -1) {
        return memo[i][j];
    }
    
    int pickLeft = nums[i] - maxDiff(nums, i + 1, j, memo);
    int pickRight = nums[j] - maxDiff(nums, i, j - 1, memo);
    
    memo[i][j] = MAX(pickLeft, pickRight);
    return memo[i][j];
}

bool predictTheWinner(int* nums, int numsSize) {
    if (numsSize % 2 == 0) {
        return true;
    }
    
    int memo[20][20];
    memset(memo, -1, sizeof(memo));
    
    return maxDiff(nums, 0, numsSize - 1, memo) >= 0;
}
