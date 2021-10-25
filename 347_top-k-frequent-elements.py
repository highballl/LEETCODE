from collections import Counter

nums = [1, 1, 1, 2, 2, 3]
k = 2

elems = Counter(nums).most_common(k)
result = [elem for elem, _ in elems]
print(result) 


