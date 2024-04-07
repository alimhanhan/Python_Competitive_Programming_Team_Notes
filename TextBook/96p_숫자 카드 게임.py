n, m = 3, 3
array = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]

result = 0

for i in range(n):
    min_value = min(array[i])  # 각 행의 최소 값을 찾기 위해 array[i]로 수정
    result = max(result, min_value)

print(result)
