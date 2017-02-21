
def emptyList(amount, emptyString):
	_list = []
	for item in range(amount):
		_list.append(emptyString)
	return _list

class Queue:

	def __init__(self):
		self.maxQueueSize = 10
		self.__emptyString = "empty"
		self.queue = emptyList(self.maxQueueSize, self.__emptyString)
		self.front = 0
		self.rear = -1

	""" A function to add an item to the queue """
	def enQueue(self, item):
		if self.isFull():
			return False
		self.rear += 1
		self.queue[self.rear] = item
		return True

	""" A function to remove and return an item from the front """
	def deQueue(self):
		if self.isEmpty():
			return False

		item = self.queue[self.front]
		self.queue[self.front] = self.__emptyString
		self.front += 1
		return item

	""" A function that indicates whether the queue is empty! """
	def isEmpty(self):
		if self.rear == self.front - 1:
			return True
		return False

	""" A function that indicates whether the queue is max! """
	def isFull(self):
		if (self.rear - self.front) == self.maxQueueSize - 1 :
			return True
		return False


nq = Queue()
nq.enQueue("HEY JOSH")

for i in range(5):
	nq.enQueue(i)

print(nq.queue)

while not nq.isEmpty():
	print("- - - - - - - - -")
	print(nq.deQueue())
	print(nq.queue)
	print("Front >", nq.front)
	print("Rear >", nq.rear)
	input(">")

nq.enQueue("test")
print(nq.queue)
print(nq.deQueue())
print(nq.queue)
