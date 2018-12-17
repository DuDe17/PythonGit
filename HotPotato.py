size = int(input())

lst = []

for _ in range(size):
    lst.append(input())

killIndex = int(input())
print(lst)
index = 0
for _ in range(size - 1):
    index = (index + killIndex) % len(lst) - 1
    if index < 0:
        index = len(lst) - 1
    del  lst[index]
    print(lst)

print(lst)    
