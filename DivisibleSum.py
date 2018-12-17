arr, div = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
for i in range(arr):
    for j in range(i,arr):
        if i != j:
            total = lst[i] + lst[j]
            if total % div == 0:
                count += 1
print(count)
