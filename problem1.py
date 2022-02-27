## Problem1 (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)


class Solution:
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}                              #keep it in the hasmap
        for num in nums:                    
            d[num] = 1
            
        out = []
        for i in range(1, n+1):             #loop through all the numbers from 1 to n
            if i not in d:                  #save the number which are not present in the dict
                out.append(i)
                
        return out                          #return the output
    """
    
    #O(N) time complexity
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        i = 0               #start with the first index
        while i < n:
        
            #while the nums[i] and nums[ nums[i] - 1 ] are not at their correct position
            while nums[i] != i+1 and nums[ nums[i] - 1 ] != nums[i]:
                other_idx = nums[i] - 1
                #keep swapping both the numbers
                nums[i], nums[ other_idx ] = nums[ other_idx ], nums[i]
                
            i += 1
            
        out = []
        #loop through all the elements and find the numbers not present in the array
        #corresponding to their index
        for idx, num in enumerate(nums):
            if idx + 1 != num:
                out.append( idx + 1 )
                
        return out