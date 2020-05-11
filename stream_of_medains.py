class Heap:
	def __init__(self, L=[]):
		self.A = L
		
	def __str__(self):
		return str(self.A)
	
	def __len__(self):
		return len(self.A)

	def heapify_down(self, k, n):
		while 2*k+1 < n:
			L = 2*k + 1
			R = 2*k + 2
			if( L < n and self.A[L] > self.A[k]):
				m = L
			else:
				m = k
			if( R < n and self.A[R] > self.A[m]):
				m = R
			if m != k:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				k = m
			else: break

	def make_heap(self):
		n = len(self.A)
		for k in range(n-1, -1, -1):
			self.heapify_down(k, n)

	def heap_sort(self):
		n = len(self.A)
		for k in range(len(self.A)-1, -1, -1):
			self.A[0],self.A[k] = self.A[k], self.A[0]
			n = n -1
			self.heapify_down(0, n)

	def heapify_up(self, k):
		while k > 0 and self.A[(k-1) // 2] < self.A[k] :
			self.A[k], self.A[(k-1) // 2] = self.A[(k-1) // 2], self.A[k]
			k = (k-1) // 2

	def insert(self, key):
		self.A.append(key)
		self.heapify_up(len(self.A) - 1)
		
	def delete_max(self):
		if len(self.A) == 0:
			return None
		key = self.A[0]
		self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		self.A.pop()	# 실제로 리스트에서 delete!
		self.heapify_down(0, len(self.A)) # len(self.A) = n-1
		return key


S = [int(x) for x in input().split()]

Max = Heap([])
Min = Heap([])
median = []

for i in range(len(S)):
	if len(Max) == 0:
		Max.insert(S[i])
	elif S[i] > Max.A[0]:
		Min.insert(-1 * S[i])
	else:
		Max.insert(S[i])
		
	if len(Min) == 0:
		pass
	elif Max.A[0] > -1 * Min.A[0]:
		Min.insert(-1 * Max.delete_max()), Max.insert(-1 * Min.delete_max())
		
	if len(Max) - len(Min)>1:
		Min.insert(-1 * Max.delete_max())
	elif len(Min) - len(Max) > 0:
		Max.insert(-1 * Min.delete_max())
		
	median.append(Max.A[0])

Sum = 0

for i in range(len(median)):
	Sum += median[i]

print(Sum)
	
