# 가위치법을 사용하여 근 (f(x) = 0 이 되는 x값) 구하기
import math

x_list = [] # 근사값 저장 배열
x_list.append(0) # 초기값은 0으로 설정
error_list = [] # 오차값 저장 배열

# f(x) = xe^-x + 1 에 대한 함수
def f(x) :
    return x * math.exp(-x) + 1

# f(x1)과 f(x2)를 연결한 직선과 축이 만나는 교점 x3
def set_x3(x1, x2) :
    x3 = x2 - f(x2)*((x2-x1)/(f(x2)-f(x1)))
    return x3

# 상대 오차를 계산하기 위한 함수
def error(approximate_value, true_value) :
    absolute_error = (approximate_value - true_value) # 절대오차 구하기
    relative_error = abs(absolute_error / true_value) * 100 # 상대오차 구하기
    return relative_error
    
# 초기 x값에 대한 구간을 입력
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))

# 범위 내에 근이 존재하는지 여부 확인
# 1. x범위 양 끝값에서의 함수값의 곱이 음수
if ((f(x1) * f(x2)) < 0) :
    print("해당 범위내에 근이 존재합니다.")
    while True :
        x3 = set_x3(x1, x2) # x축과 만나는 x3값 구하기
        x_list.append(x3) # x 리스트에 추가
        
        if (f(x3) == 0) : # x3값에서 함수값이 0 이라면 근을 설정하고 반복문 종료
            x = x3 # x값(근) 설정
            print(f"근은 {x} 입니다.")
            break # 종료
        
        elif (f(x1) * f(x3) < 0) : # f(x1)값과 f(x3)값의 곱이 음수라면 해당 범위내에 근이 존재하므로 x2 = x3
            x2 = x3
            
        elif (f(x1) * f(x3) > 0) : # f(x1)값과 f(x3)값의 곱이 양수라면 해당 범위내에 근이 없으므로 x1 = x3
            x1 = x3
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