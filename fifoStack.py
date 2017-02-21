class Stack:
	#Last in first out stack
	def __init__(self):
		self.maxSize = 10
		self.stack = []

	def push(self, item):
		if not self.isFull():
			self.stack.append(item)
			return True
		return False		


	def pop(self):
		item = self.peek()
		self.stack = self.stack[1:]
		return item

	def isFull(self):
		if len(self.stack) == self.maxSize:
			return True
		return False

	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		return False

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[0]

st = Stack()

for i in range(20):
	print("push", i, st.push(i))

print("is full", st.isFull())

for i in range(st.maxSize):
	print(st.pop())

print("is empty", st.isEmpty())
