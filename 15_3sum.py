from collections import deque, Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        whole = Counter(nums)
        keys = deque(sorted(list(whole)))
        check = []
        result = []

        if 0 in keys and whole[0] > 2 and set({0, 0, 0}) not in check:
            result.append([0, 0, 0])
            check.append(set({0,0,0}))
            


        for i in range(len(keys)):
            km = keys[i]
            left, right = i, len(keys)-1
            while left <= right:
                kl, kr = keys[left], keys[right]
                if kl+km+kr == 0 and set({kl, kr, km}) not in check:
                    # 3 different nums
                    if km != kl and km != kr and kr != kl:
                        result.append([kl, km, kr])
                        check.append(set({kl, km, kr}))
                    # 2 same 1 diff nums
                    elif (km == kl and km != kr and whole[kl] > 1) or (km == kr and km != kl and whole[kr] > 1) or (kl == kr and kl != km and whole[kl] > 1):
                        result.append([kl, km, kr])
                        check.append(set({kl, km, kr}))
                if abs(kl+km) > kr:
                    left += 1
                elif abs(kl+km) <= kr:
                    right -= 1

        return result