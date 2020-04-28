 # 1. class Node 선언 부분
class Node:
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value
		self.prev = self
		self.next = self
		
	def __str__(self):
		return str(self.key)
	
# 2. class DoublyLinkedList 선언부분
class DoublyLinkedList:
	def __init__(self):
		self.head = Node()	# dummy 노드로만 이루이진 빈 리스트
		self.size = 0
		
	def __len__(self):
		return self.size
	
	def size(self):
		return self.size
	
	def splice(self, a, b, x): # cut [a..b] after x
		if a == None or b == None or x == None: 
			return
		# 1. [a..b] 구간을 잘라내기 
		a.prev.next = b.next
		b.next.prev = a.prev
		# 2. [a..b]를 x 다음에 삽입하기
		x.next.prev = b
		b.next = x.next
		a.prev = x
		x.next = a
		
	def moveAfter(self, a, x):
		DoublyLinkedList.splice(self, a, a, x)
		
	def moveBefore(self, a, x):
		DoublyLinkedList.splice(self, a, a, x.prev)
		
	def insertBefore(self, k, val):
		DoublyLinkedList.moveBefore(self, Node(val), k)
		
	def insertAfter(self, k, val):
		DoublyLinkedList.moveAfter(self, Node(val), k)
		
	def pushFront(self, key):
		DoublyLinkedList.insertAfter(self, self.head, key)
		
	def pushBack(self, key):
		DoublyLinkedList.insertBefore(self, self.head, key)
		
	def deleteNode(self, x): # delete x
		if x == None or x == self.head: 
			return
		x.prev.next, x.next.prev = x.next, x.prev
		del x

	def popFront(self):
		if self.head.next == self.head: 
			return None
		key = self.head.next.key
		DoublyLinkedList.deleteNode(self, key)
		return key
	
	def popFront(self):
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			v = self.head.next
		DoublyLinkedList.deleteNode(self, v)
		return v
	
	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			v = self.head.prev
		DoublyLinkedList.deleteNode(self, v)
		return v
		
	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head	#Dummy Node
		if key == v.prev.key:
			return v.prev
		while v.next != self.head:
			if v.key == key:
				return v
			v = v.next
		return None	#search failed
		
	def first(self):
		v = self.head
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			return v.next
		
	def last(self):
		v = self.head
		if DoublyLinkedList.isEmpty(self) == True:
			return None
		else:
			return v.prev
		
	def isEmpty(self):
		if self.head == self.head.next:
			return True
		else:
			return False
		
	def printList(self):
		v = self.head.next
		print("h", "->", end=" ")
		while(v != self.head.prev):
			print(v.key, "->", end=" ")
			v = v.next
		print(v.key, "->", end=" ")
		print("h")

L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print(" * {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")
