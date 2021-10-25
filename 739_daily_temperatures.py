T = [73, 74, 75, 71, 69, 72, 76, 73]

result = []
cnt = 1
for i in range(1, len(T)):
    if T[i] > T[i-1]:
        result.append(cnt)
        cnt = 1
    else:
        if T[i] >= max(T[i:]) or i == len(T)-1:
            result.append(0)
        else:
            k = 1
            temp_cnt = 1
            while T[i-1] < T[i-1+k]:
                temp_cnt += 1
                k += 1
        
            result.append(temp_cnt)
        cnt += 1

print(result)