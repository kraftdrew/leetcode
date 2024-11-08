#1. Two Sum ------------------------------
# https://leetcode.com/problems/two-sum/

# Solution 1: (Brute Force)
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return [] # No solution found



# Solution 2: (One-pass Hash Table)

def twoSumHash(nums: List[int], target: int) -> List[int]:
    hashMap = {}
    array_len = len(nums)

    for i in range(array_len):
        difference = target - nums[i]  
        if difference in hashMap: 
            return [hashMap[difference] , i]
        
        hashMap[ nums[i]] = i   
    
    return [] # no value found

            
        
print(twoSumHash([2,7,8,10],10))


