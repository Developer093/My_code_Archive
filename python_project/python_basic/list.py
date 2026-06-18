# list >> 여러개 의 데이터를 저장할 수 있는 자료형
# list는 []로 표현한다.
# index >> 리스트 안에 있는 각 요소의 번호
# 0부터 시작한다.

# list 기본 형태
list = [1, 2, 3, 4, 5]
print(list[0])

# 1. 값 변경하기
# list는 값을 변경할 수 있다.
# list명.index = 변경할 값

replace_list = ["지환", "현균", "상원"]
replace_list[1]= "현호"
print(replace_list)

# 2. append() >> 리스트에 요소를 추가하는 메서드
# list명.append(추가할 요소)
# append()는 리스트의 마지막에 요소를 추가한다.

append_list = ["지환", "현균", "상원"]
append_list.append("준엽")
print(append_list)

# ※여러번 추가할 수 있다.▼
append_list.append("지환")
append_list.append("현균")
print(append_list)

# 3. remove() >> 리스트에 요소를 제거하는 메서드
# list명.remove(제거할 요소)
# 인덱스가 아닌 요소를 직접 입력해야 한다.

remove_list = ["지환", "현균", "상원", "시진", "대웅"]
remove_list.remove("시진")
print(remove_list)

# 4. len() >> 리스트 길이를 구하는 메서드
# len(리스트 명)

len_list = ['a','b','c','d']
print(len(len_list))

# 5. 반복문과 사용 해보기
# for 변수 in 리스트:
#    실행할 코드

repeat_list = [10, 20, 30]

for repeat_list in repeat_list:
    print(repeat_list)