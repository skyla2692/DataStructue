class Stack:
	def __init__(self):
		self.items = []	# 데이터 저장을 위한 리스트 준비
	def push(self, val):
		self.items.append(val)
	def pop(self):
		try:	# pop할 아이템이 없으면
			return self.items.pop()
		except IndexError:	# indexError 발생
			print("Stack is empty")
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
	def __len__(self):	# len()로 호출하면 stack의 item 수 반환
 		return len(self.items)
	def isEmpty(self):
		return self.__len__() == 0

def get_token_list(expr):
    token = []
    ops = '+-*/^'
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isdigit() or c == ".":
            val, i = get_value(expr, i)
            token.append(val)
        elif c in ops:
            token.append(c)
            i += 1
        elif c.isspace():
            i += 1
        else:
            print("Invalid Expression!")
            break
    return token

def infix_to_postfix(token_list):
	opstack = Stack()
	outstack = []
	# 연산자의 우선순위 설정
	prec = {}
	prec['('] = 0
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 3

	for token in token_list:
		if token == '(':
			opstack.push(token)
        
		elif token == ')':
            top = opstack.pop()
			while top != '(':
				outstack.append(top)
                top = opstack.pop()
			
		elif token in '+-/*^':
            while not opstack.isEmpty() and prec[opstack.top()] >= prec[token]:
                outstack.append(opstack.pop())
            opstack.push(token)
		else:
			outstack.append(token)
			
	while not opstack.isEmpty():
		outstack.append(opstack.pop())
	return (outstack)

def compute_postfix(postfix):
	S = Stack()
    for op in token_list:
        if op in '+-*/^':
            try:
                t = S.pop()
                b = S.pop()
				if op == '+':
                    S.push(b+t)
				elif op == '-':
                    S.push(b-t)
                elif op == '*':
                    S.push(b*t)
				elif op == '/':
					S.push(b/t)
				elif op == '^':
					S.push(b**t)
                else:
                    print(op, "is not allowed")
                    return None
            except IndexError:
                print("Invalid postfix expression")
                return operand_s.pop()
        else:
            try:
                operand = float(sym)
                S.push(operand)
            except ValueError:
                print("Not float operand")
                return None
    return S.pop()
    
def get_value(E, i):
    j = i + 1
    while j < len(E) and (E[j].isdigit() or E[j] == '.'):
        j += 1
    return E[i:j], j
    
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
