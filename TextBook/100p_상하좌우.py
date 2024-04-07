n = int(input())
plans = input().split()

x, y = 1, 1

for direction in plans:
    if direction == 'L' and y > 1:
        y -= 1
    elif direction == 'R' and y < n:
        y += 1
    elif direction == 'U' and x > 1:
        x -= 1
    elif direction == 'D' and x < n:
        x += 1

print(x, y)
