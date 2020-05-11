import time, random

def sum(A, n):
	B = []
	for i in range(0, n):
		row_list = []
		for j in range(i):
			row_list.append(0)
		for j in range(i, n):
			row_list.append(0)
			row_list[j] = row_list[j-1]
			row_list[j] += A[j]
		B.append(row_list)
	
# n = 1 이상 5000 이하 정수 값 입력
n = int(input())
# 리스트 A에 랜덤 정수 값 n개 채움
A = []
for i in range(n):
	A.append(random.randint(0, 101))

print(A)
# sum 함수 호출 + 시간 측정
before = time.process_time()
sum(A, n)
after = time.process_time()

# 함수의 수행시간을 출력
print(after - before)
