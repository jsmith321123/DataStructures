import time
import pprint
import random

class HashTable:
	def __init__(self):
		self.table = []
		self.size = 10000
		for i in range(0, 10000):
			self.table.append("empty")

	def hash(self, id):
		return id % self.size

	def add(self, data): #data is a dictionary
		id = data["id"]
		key = self.hash(id)
		repeats = 0		
 		
		while self.table[key] != "empty" and repeats < 2:
			key += 1
			oldKey = key
			key = key % self.size
			if(key != oldKey):
				repeats += 1
		
		if(repeats < 2):
			self.table[key] = data
		else:
			print("Table Full")

	def find(self, id):
		key = self.hash(id)
		repeats = 0
		while self.table[key]["id"] != id and repeats < 2:
                	key += 1
			oldKey = key
			key = key % self.size
			if oldKey != key:
				repeats += 1			
		if repeats < 2:
			return self.table[key]
		else:
			return "Not found"
	
		

ht = HashTable()

ht.add({"id": 992, "blah": "blorg"})

for i in range(0, 10001):
	ht.add({"id": random.randint(0, 1000000), "blah": "blorg"})
	if i % 1000 == 0:
		print(i)

initTime = time.time()
print(ht.find(992))
print(ht.find(9000000))
print(time.time() - initTime, " seconds")
