arr = int(input())
lst = list(map(int, input().split()))
day, month = map(int, input().split())

count = 0
for i in range(arr-month+1):
    total = 0
    for j in range(month):
        total += lst[i+j]
    if total == day:
        count += 1
print(count)
