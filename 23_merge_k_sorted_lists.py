import heapq

lists = [[1,4,5],[1,3,4],[2,6]]
heap_list = []
for idx, list in enumerate(lists):
    for elem in list:
        heapq.heappush(heap_list, elem)

result = []
while heap_list:
    result.append(heapq.heappop(heap_list))

print(result)
