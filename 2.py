#https://leetcode.com/problems/3sum/submissions/
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i, given_n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - given_n
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    ans.append( [ given_n, nums[lo], nums[hi] ] )
                    while lo < len(nums)-1 and nums[lo] == nums[lo+1]:
                        lo += 1
                    while hi > 0 and nums[hi-1] == nums[hi]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1
        return ans
                
                
                
