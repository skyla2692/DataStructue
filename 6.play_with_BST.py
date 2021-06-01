# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0  # 높이 정보도 유지함에 유의!!

	def __str__(self):
		return str(self.key)

class Tree:
	def __init__(self):
		self.root = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		return self.root.__iter__()

	def preorder(self, v):
		if v != None:
			print(v.key, end=' ')
			self.preorder(v.left)
			self.preorder(v.right)

	def inorder(self, v):
		if v != None:
			self.inorder(v.left)
			print(v.key, end=' ')
			self.inorder(v.right)

	def postorder(self, v):
		if v != None:
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end=' ')

	def insert(self, key):
		v = Node(key)
		if self.size == 0: 
			self.root = v
		else:
			p = self.find_loc(key)
			if p and p.key != key: # p is parent of v
				if p.key < key: p.right = v
				else: p.left = v
				v.parent = p
		self.size += 1
		return v

	def find_loc(self, key): # if key is in T, return its Node
	# if not in T, return the parent node under where it is inserted
		if self.size == 0: return None
		p = None    # p = parent node of v
		v = self.root
		while v:    # while v != None
			if v.key == key: return v
			else:
				if v.key < key:
					p = v
					v = v.right
				else:
					p = v
					v = v.left
		return p

	def search(self, key):
		p = self.find_loc(key)
		if p and p.key == key:
			return p
		else:
			return None
	# 노드들의 height 정보 update 필요
       
T = Tree()

while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		v = T.insert(int(cmd[1]))
		if v != None:
			print("+ {0} is set into H".format(v.key))
		else:
			print(key, "is already in the tree!")
	elif cmd[0] == 'search':
		v = T.search(int(cmd[1]))
		if v == None:
			print("* {0} is not found!".format(cmd[1]))
		else:
			print(" * {0} is found!".format(cmd[1]))
	elif cmd[0] == 'preorder':
		T.preorder(T.root)
		print()
	elif cmd[0] == 'postorder':
		T.postorder(T.root)
		print()
	elif cmd[0] == 'inorder':
		T.inorder(T.root)
		print()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")
