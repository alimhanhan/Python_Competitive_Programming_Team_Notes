input_data = input()  # 사용자로부터 좌표를 입력받음. 예: 'a1'
row = int(input_data[1])  # 입력된 좌표의 행 번호를 가져옴. 예: '1'

# 입력된 좌표의 열 번호를 가져옴. ord 함수를 사용하여 알파벳을 숫자로 변환함. 'a'의 ASCII 코드는 97.
column = int(ord(input_data[0])) - int(ord('a')) + 1


steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]  # 나이트가 이동할 수 있는 8가지 방향을 정의함.

result = 0  # 가능한 이동 경로의 수를 저장할 변수를 초기화함.

# 각 방향에 대해 이동이 가능한지 확인하고, 가능한 경우 result에 1을 더함.
for step in steps:
    next_row = row + step[0]  # 다음 이동할 행 번호 계산
    next_column = column + step[1]  # 다음 이동할 열 번호 계산

    # 다음 위치가 체스판 내에 있는지 확인함.
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1  # 다음 위치가 체스판 내에 있으면 결과에 1을 더함.

print(result)  # 결과 출력
