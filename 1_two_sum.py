from collections import deque

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        filtered = deque(sorted(nums))
        
        while filtered:
            left = filtered[0]
            right = filtered[-1]
            if left+right == target:
                if left == right:
                    return [idx for idx, val in enumerate(nums) if val == left][:2]
                    break
                return sorted([nums.index(left), nums.index(right)])
                break
            elif left+right > target:
                filtered.pop()
            # left + right < target
            else: 
                filtered.popleft()

#Runtime: 64 ms, faster than 57.22% of Python3 online submissions for Two Sum.
#Memory Usage: 14.9 MB, less than 66.16% of Python3 online submissions for Two Sum.