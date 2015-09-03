import sys

class Stack:
	
	def __init__(self):
		#initiates stack
		self.myStack = []
		
	def pop(self):
		#pops value off the top of stack
		return self.myStack.pop()
		
	def push(self, x):
		#adds element to the top of the stack
		return self.myStack.append(x)
			
	def checkSize(self):
		#prints the size of the stack
		print len(self.myStack)
		return
		
	
if __name__ == "__main__":
	c = Stack()
	c.push(1)
	c.push(2)
	c.push(3)
	c.push(4)
	c.push(5)
	c.push(6)
	c.push(7)
	c.push(8)
	c.push(9)
	c.push(10)
	c.checkSize()
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	print("Popped off: %s" % c.pop())
	c.checkSize()
	
