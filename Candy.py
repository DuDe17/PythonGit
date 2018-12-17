lst = []
kids, boxes = map(int, input().split())
total = 0
for i in range(boxes):
    inp = int(input())
    lst.append(inp)
    total += inp

print(int(total/kids))
