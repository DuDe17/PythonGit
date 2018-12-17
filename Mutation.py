def compare(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count += 1
        else:
            count -= 1
    if count == (len(str1)-2):
        return True
    else:
        return False

dna = input()
virus = input()

if virus in dna:
    print(dna.index(virus)+1)
else:
    index = -1
    length = len(virus)
    for i in range(len(dna) - length + 1):
        if dna[i] == virus[0]:
            if compare(dna[i:i+length], virus):
                index = i + 1
                break
    print(index)
