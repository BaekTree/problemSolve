#https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for up_i in range(len(nums) - 3):
            if up_i > 0 and ( nums[up_i - 1] == nums[up_i] ):
                continue
                
            if nums[up_i] * 4 > target:
                break
            up_target = target - nums[up_i]
            
            
            for down_i in range(up_i + 1, len(nums) - 2):
                
                if down_i > up_i + 1 and ( nums[down_i - 1] == nums[down_i] ):
                    continue
                if nums[down_i] * 3 > up_target:
                    break                
                down_target = up_target - nums[down_i]

                
                
                left = down_i + 1
                right = len(nums) - 1
                
                while left < right:
                    
                    if nums[left] + nums[right] > down_target:
                        right -= 1
                    elif nums[left] + nums[right] < down_target:
                        left += 1
                    else:
                        res.append([nums[up_i], nums[down_i], nums[left], nums[right]])
                        
                        left += 1
                        while left < len(nums) - 1 and ( nums[left - 1] == nums[left] ):
                            left += 1
                            
                        right -= 1
                        while right > 0 and ( nums[right + 1] == nums[right] ):
                            right -= 1
                
                
                
                    
                        
                        
            

        return res
