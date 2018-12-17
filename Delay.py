sHr, sMi = map(int,input().split())
eHr, eMi = map(int,input().split())

startTime = (sHr*60) + sMi
endTime = (eHr*60) + eMi

delay = int(input())
flightTime = int(input())

if ((startTime + delay + flightTime) < endTime):
    print('YES')
else:
    print('NO')
