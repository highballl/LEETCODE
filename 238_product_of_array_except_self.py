class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []

        temp = Counter(nums)

        for num in nums:
            mul = 1
            for k, v in temp.items():
                if num == k:
                    mul *= reduce(lambda x, y: x**y, [k, v-1])
                else:
                    mul *= reduce(lambda x, y: x**y, [k, v])
            result.append(mul)

        return result