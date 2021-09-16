#https://leetcode.com/problems/3sum-closest/submissions/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
            더해서 특정 수가 나오는 두 수를 찾아야 한다.
            정렬 되어 있다.
            
            양쪽 끝에서 시작.
            더해서 수가 크면 큰 수를 낮춘다.
            같은 수면 계속 낮춘다.
            작으면 작은 수를 키운다.
            같은 수면 계속 키운다.
            
            left < right이면 계속 반복.
            
            while left < right
                
                if nums[left] + nums[right] == sum
                    # found!
                    answer.append( [ nums[left], nums[right] ] )
                    
                elif nums[left] + nums[right] > sum
                    min_distance = min(min_distance, left + right - sum)
                    right -= 1
                    while nums[right+1] == nums[right]
                        right -= 1
                        
                else
                    min_distance = min(min_distance, sum - left + right)
                    left += 1
                    while nums[left-1] == nums[left]
                        left += 1
                
        
        """
        orig_target = target
        nums = sorted(nums)
        # answer = []
        min_distance = float('inf')

        answer = 0
        for i, n in enumerate(nums):
            
            target = orig_target - n
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] == target:
                    min_distance = 0
                    answer = target + n
                    break

                elif nums[left] + nums[right] > target:
                    if min_distance > abs(nums[left] + nums[right]- target):
                        answer = nums[left] + nums[right] + n
                        min_distance = abs(nums[left] + nums[right] - target)
                    right -= 1

                else:
                    if min_distance > abs(target - (nums[left] + nums[right])):
                        answer = nums[left] + nums[right] + n
                        min_distance = abs(nums[left] + nums[right] - target)
                    left += 1
        return answer
