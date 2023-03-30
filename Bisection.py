# 이분법을 사용하여 근 (f(x) = 0 이 되는 x값) 구하기
import math

x_list = [] # 근사값 저장 배열
x_list.append(0) # 초기값은 0으로 설정
error_list = [] # 오차값 저장 배열

# f(x) = xe^-x + 1 에 대한 함수
def f(x) :
    return x * math.exp(-x) + 1

# 범위의 중간값 구하는 함수
def center(x1, x2) :
    x_center = (x1 + x2) / 2
    return x_center

# 상대 오차를 계산하기 위한 함수
def error(approximate_value, true_value) :
    absolute_error = (approximate_value - true_value) # 절대오차 구하기
    relative_error = abs(absolute_error / true_value) * 100 # 상대오차 구하기
    return relative_error
    
# 초기 x값에 대한 구간을 입력
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))

# 범위 내에 근이 존재하는지 여부 확인
# 1. 초기 x범위 양 끝값에서의 함수값의 곱이 음수 and, 
# 2. 초기 x범위의 중간값이 0이 아닌경우
if ((f(x1) * f(x2)) < 0) and (f(center(x1, x2)) != 0) :
    print("해당 범위내에 근이 존재합니다.")
    while True :
        x_center = center(x1, x2) # 범위 중간값 구하기
        x_list.append(x_center) # x 리스트에 추가
        
        if (f(x_center) == 0) : # 중간값의 함수값이 0 이라면 근을 설정하고 반복문 종료
            x = x_center # x값(근) 설정
            print(f"근은 {x} 입니다.")
            break # 종료
        
        elif (f(x1) * f(x_center) < 0) : # f(x1)값과 f(x_center)값의 곱이 음수라면 해당 범위내에 근이 존재하므로 x2 = x_center
            x2 = x_center
            
        elif (f(x1) * f(x_center) > 0) : # f(x1)값과 f(x_center)값의 곱이 양수라면 해당 범위내에 근이 없으므로 x1 = x_center
            x1 = x_center
else :
    print("근을 찾을 수 없습니다.")
    
# 오차 계산 및 저장
for i in range(len(x_list)-1) : 
    error_list.append(error(x_list[i], x_list[i+1]))

# 오차 출력
for i in range(len(error_list)) :
    print(f"{i+1}번째 오차 : {error_list[i]} %")
    if i == 9 : # 10개 까지 출력후 종료 
        break