class Stack:
	def __init__(self):
		self.items = []
		
	def push(self, val):
		self.items.append(val)
		
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")
			
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
			
	def __len__(self):
		return len(self.items)
		
	def isEmpty(self):
		return self.__len__() == 0

def compute_postfix(postfix):
	operand_s = Stack()
	if len(postfix) <= 1 :
		return postfix[0]
	elif len(postfix) > 1:
		for op in postfix:
			if op in '+-*/^':
				operand_1 = float(operand_s.pop())
				operand_2 = float(operand_s.pop())
				if op == '+':
					calculated_operand = operand_1 + operand_2
				elif op == '-':
					calculated_operand = operand_2 - operand_1
				elif op == '*':
					calculated_operand = operand_1 * operand_2
				elif op == '/':
					calculated_operand = operand_2 / operand_1
				elif op == '^':
					calculated_operand = operand_2 ** operand_1
				operand_s.push(calculated_operand)
			else:
				operand_s.push(op)
		return operand_s.pop()
	
postfix = [x for x in input().split()]
print("{:.4f}".format(compute_postfix(postfix)))
