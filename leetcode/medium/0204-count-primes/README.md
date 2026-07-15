# Count Primes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer `n`, return  *the number of prime numbers that are strictly less than*  `n`.

 

 **Example 1:** 

```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

```

 **Example 2:** 

```
Input: n = 0
Output: 0

```

 **Example 3:** 

```
Input: n = 1
Output: 0

```

 

 **Constraints:** 

- 0 <= n <= 5 * 106

## Solution

**Language:** Java  
**Runtime:** 93 ms (beats 84.10%)  
**Memory:** 51.3 MB (beats 38.11%)  
**Submitted:** 2026-07-15T05:15:13.574Z  

```java
class Solution {
    public int countPrimes(int n) {
        if(n<2)
            return 0;
        boolean isprime[] = new boolean[n];
        Arrays.fill(isprime,true);
        for(int i=2;i<=Math.sqrt(n);i++)
        {
            if(isprime[i])
            {
                for(int j=i*i;j<n;j+=i)
                    isprime[j]=false;
            }
        }
        int count = 0;
        for(int i=2 ;i<n;i++)
            if(isprime[i])
                count++;

                return count;
    }

}
```

---

[View on LeetCode](https://leetcode.com/problems/count-primes/)