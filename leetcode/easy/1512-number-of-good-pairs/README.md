# Number of Good Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `nums`, return  *the number of  **good pairs***.

A pair `(i, j)` is called  *good*  if `nums[i] == nums[j]` and `i` < `j`.

 

 **Example 1:** 

```
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

```

 **Example 2:** 

```
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

```

 **Example 3:** 

```
Input: nums = [1,2,3]
Output: 0

```

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

## Solution

**Language:** Java  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 42.8 MB (beats 62.29%)  
**Submitted:** 2026-07-20T05:41:52.266Z  

```java
import java.util.*;
class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;

        for(int num:nums){
            int freq = map.getOrDefault(num,0);
            count += freq;
            map.put(num ,freq+1);
        }
        return count;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-good-pairs/)