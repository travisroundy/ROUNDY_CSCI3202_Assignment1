import sys

class Queue:
	
	def __init__(self):
		#initiates queue
		self.myQueue = []
		
	def Add(self, x):
		#Inserts value to queue after values already present
		return self.myQueue.insert(0, x)
		
	def Remove(self):
		#if the queue isnt empty, takes value from front out
		if (len(self.myQueue) != 0):
			return self.myQueue.pop()
		#otherwise if queue is empty it prints a statement
		else:
			print("Cannot dequeue an empty queue!")
		
		
		
	
if __name__ == "__main__":
	c = Queue()
	c.Add(1)
	c.Add(2)
	c.Add(3)
	c.Add(4)
	c.Add(5)
	c.Add(6)
	c.Add(7)
	c.Add(8)
	c.Add(9)
	c.Add(10)
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
	print("Dequeued: %s" % c.Remove())
