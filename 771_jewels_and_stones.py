from collections import defaultdict

J = 'aA'
S = 'aAAbbbb'

# make jewel dict
jewel = defaultdict()
for j in J:
    jewel[j] = j

# count jewels in stone
cnt = 0
for s in S:
    try:
        if jewel[s]:
            cnt += 1
    except:
        continue

print(cnt)
