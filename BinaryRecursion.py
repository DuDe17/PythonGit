def binary(n):
    resource = '01'
    if n < 2:
        return resource[n]
    else:
        return binary(n//2) + resource[n%2]

print(binary(int(input())))
