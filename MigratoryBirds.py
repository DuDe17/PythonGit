arr = int(input())
lst = list(map(int, input().split()))

key = []
value = []

for i in range(arr):
    if lst[i] not in key:
        key.append(lst[i])
        value.append(1)
    else:
        value[key.index(lst[i])] += 1

total = 0
out = 0

for i in range(len(value)):
    if value[i] > total:
        total = value[i]
        out = key[i]
    elif value[i] == total:
        if key[i] < out:
            out = key[i]

print(out)
