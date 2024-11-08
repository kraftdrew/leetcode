# 1. Two Sum ------------------------------
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

            
        
# print(twoSumHash([2,7,8,10],10))



# 9. Palindrome Number ------------------------------
# https://leetcode.com/problems/palindrome-number/description/


# Solution 1: Reversing the Entire Number

def isPalindrome(x: int) -> bool:

    if x < 0:
        return False
    
    reversed = 0 
    temp = x
    # 121
    while temp != 0: 
        digit = temp % 10   # 1
        reversed = reversed * 10 + digit
        temp //= 10
    if x == reversed:
        return True
    
    return False
            
            
# Approach 2: Reversing Half of the Number

def isPalindrome( x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    reversed_half = 0 
    temp = x 

    # 1230321
    while temp > reversed_half:
        reversed_half = reversed_half * 10 + temp % 10  # 1, 12, 123, 1230; 
        temp //= 10   # 123032, 12303, 1230, 123

    if  temp == reversed_half or temp == reversed_half // 10: 
        return True
    
    return False

#print(isPalindrome(123))



# ------------------------------