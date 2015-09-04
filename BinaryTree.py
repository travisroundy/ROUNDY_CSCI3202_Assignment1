#I was not able to complete the Binary Tree class. I kept running into
#dead ends. Although if it were to work correctly, creating an instance
#of the Binary Tree would also create an instance of the Node class and
#would be the root of the tree. To add to the tree, I would call a 
#pre-order traversal function in order to find the parentValue given. 
#From there check the left and right nodes to add, otherwise print
#that the node has two children. Removing would be a similar process,
#however rather than going through and adding a node if there are no
#children, it would check to see if it had children and execute from there.
#Printing the tree would use a similar preorder function, but would print
#the values rather than returning.

import sys

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
	
class BinaryTree:
	
	def __init__(self, value):
		print("Added %s" % value)
		self.root = Node(value)
		self.currentNode = 0
	
	def add(self, value, parentValue):
		
		self.currentNode = parentValue
		self.currentNode = self.preorder(self.root)
		if (self.currentNode == None):
			self.currentNode = Node(parentValue)
			self.currentNode.value = parentValue
		#print("add value: %s" % self.currentNode)
		self.currentNode.value = parentValue

		if (self.currentNode.value == parentValue) & (self.currentNode.left == None):
			self.currentNode.left = Node(value)
			self.currentNode.left.parent = value
			print ("added %s" % self.currentNode.left.value)
		elif (self.currentNode.value == parentValue) & (self.currentNode.left != None) & (self.currentNode.right == None):
			self.currentNode.right = Node(value)
			self.currentNode.right.parent = value
			print ("added %s" % value)
			
		elif (self.currentNode.value == parentValue) & (self.currentNode.left != None) & (self.currentNode.right != None):
			print ("Parent already has 2 children, node not added.")
			
		else:
			print ("Node not found!")
			
	def remove(self, value):
		if (self.currentNode.left != None):
			print ("Node has children, cannot delete node.")
		elif (self.currentNode.value == None):
			print ("Error: Node does not exist")
		else:
			print("")
		

	def preorder(self, current):
		if (current != None):
			if (current.value == self.currentNode):
				#print("currentNode value in preorder: %s" % self.currentNode)
				#print("current.value value in preorder: %s" % current.value)
				#print("current: %s" % current)
				return (current)
			elif (current != self.currentNode) & (current.left != None):
				#print("left recursion: %s" % current.value)	
				#print("currentNode value in recursion: %s" % self.currentNode)
				#print("current.left.value value in recursion: %s" % current.left.value)	
				self.preorder(current.left)
			elif (current != self.currentNode) & (current != None):
				self.preorder(current.right)
				#print("right recursion")
		else:
			current = self.currentNode
			self.preorder(current)
			
					
if __name__ == "__main__":
	tree = BinaryTree(1)
	print "----------------------------------------"
	tree.add(2,1)
	print "----------------------------------------"
	tree.add(3,1)
	print "----------------------------------------"
	tree.add(10,1)
	print "----------------------------------------"
	tree.add(4,2)
	print "----------------------------------------"
	tree.add(5,2)
	print "----------------------------------------"
	tree.remove(5)
	tree.remove(8)
	#tree.add(6,3)
	#print "----------------------------------------"
	#tree.add(7,3)
	#tree.add(8,4)
	#tree.add(0,0)
	#tree.add(9,4)
	#tree.add(10,5)
	

