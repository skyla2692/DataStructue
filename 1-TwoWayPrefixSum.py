import time, random

def prefixSum1(X, n):
	""" double for-looped prefix sum
			O(n^2) """
	for i in range(n):
		for j in range(i + 1):
			S[i] = S[i] + X[j]
	
def prefixSum2(X, n):
	""" single for-looped prefix sum
			O(n) """
	S[0] = X[0]
	for i in range(1,n):
		S[i] = S[i-1] + X[i]
	
random.seed()		#initialize random seed

n = int(input())		#get n as input
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움

X = [0] * n		#create a list X with n elements, filled with 0
S = [0] * n		#create a list S with n elements, filled with 0

for i in range(0,n):
	X[i] = random.randint(-999,999)
	#fill the list X with random integer number between -999 to 999

before1 = time.clock()		#before1 is time before we run function prefixSum1()
prefixSum1(X, n)
after1 = time.clock()		#after1 is time after we run function prefixSum1()
print("prefixSum1의 수행시간은 ", after1 - before1)		#print the difference of two variable to see the time duration of the function prefixSum1()

before2 = time.clock()		#before2 is time after we run function prefixSum2()
prefixSum2(X, n)
after2 = time.clock()		#after2 is time after we run function prefixSum2()
print("prefixSum2의 수행시간은 ", after2 - before2)		#print the difference of two variable to see the time duration of the function prefixSum2()
