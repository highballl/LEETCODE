class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = len(height)
        max_num = max(height)
        max_idx = height.index(max_num)

        count = 0
        temp_max = 0
        for i in range(max_idx):
            if height[i] > temp_max:
                temp_max = height[i]
            count += temp_max - height[i]

        temp_max = 0
        for j in range(l-1, max_idx-1, -1):
            if height[j] > temp_max:
                temp_max = height[j]
            count += temp_max - height[j]
        

        return count