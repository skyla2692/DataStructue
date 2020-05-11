class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self

class DoublyLinkedList:
	def __init__(self):
		self.head = Node()
		self.size = 0

	def splice(self, a, b, x):
		if a == None or b == None or x == None:
			return
		a.prev.next = b.next
		b.next.prev = a.prev
		x.next.prev = b
		b.next = x.next
		a.prev = x
		x.next = a
	def moveAfter(self, a, x):
		self.splice(a, a, x)
		
	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)
	
	def insertAfter(self, a, key):
		self.moveAfter(Node(key), a)
		self.size += 1

	def insertBefore(self, a, key):
		self.moveBefore(Node(key), a)
		self.size += 1
	
	def pushFront(self, key):
		self.insertAfter(self.head, key)

	def pushBack(self, key):
		self.insertBefore(self.head, key)

	def search(self, key):
		v = self.head #dummyNode
		if key == v.prev.key:
			return v.prev
		while v.next != self.head:
			if v.key == key:
				return v
			v = v.next
		return None

	def deleteNode(self, x):
		k = self.search(x)
		if k == None or k == self.head:
			return
		k.prev.next = k.next
		k.next.prev = k.prev
		self.size -= 1
		del k
	
	def popFront(self):
		if self.head.next == self.head:
			return None
		v = self.head.next.key
		self.deleteNode(self.head.next)
		return v
	
	def popBack(self):
		if self.head.next == self.head:
			return None   
		v = self.head.prev.key
		self.deleteNode(self.head.prev)
		return v
	
	def first(self):
		if self.head.next == self.head:
			return None
		return self.head.next.key

	def last(self):
		if self.head.next == self.head:
			return None
		return self.head.prev.key
	
	def printList(self):
		v = self.head.next
		print("h", "->",end=" ")
		while(v != self.head):
			print(v.key, "->", end=" ")
			v = v.next
		print("h")
	
	def __len__(self):
		return self.size

def josephus(n, k):
	L = DoublyLinkedList()
	for i in range(n): # 1번부터 n번까지의 key 값을 갖는 노드를 pushBack 함수를 써서 L에 삽입
		i += 1
		L.pushBack(i)
		
	v = L.head.next
	while(L.size != 1):
		for i in range(k-1):
			v = v.next
			if v.key == None:
				v = v.next
		L.deleteNode(v.key)
		if v.next == L.head:
			v = L.head.next
		else:
			v = v.next
	return v.key

n, k = map(int, input().split())
print(josephus(n,k))
