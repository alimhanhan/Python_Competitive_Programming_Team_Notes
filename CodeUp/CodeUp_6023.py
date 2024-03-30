s = input()
a = []

for i in range(len(s)):
    if s[i] == ':':
        a.append(s[i+1])
        a.append(s[i+2])
        break


a = [x for x in a if x != ':']

print(a[0], end="")
print(a[1], end="")