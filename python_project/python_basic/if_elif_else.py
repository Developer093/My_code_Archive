# 3. if_elif_else >> 여러 조건을 검사
# 사용법
# if val < 0:
#   실행할 코드
# elif val <= 0:
#   실행할 코드
# elif val >= 0:
#   실행할 코드
# else:
#   실행할 코드

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")