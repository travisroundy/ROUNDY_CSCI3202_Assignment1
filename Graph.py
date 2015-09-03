import sys

class Graph:
	
	def __init__(self):
		#creates a dictionary to store adjacent nodes
		self.vertexList = dict() 
		#creates a set to store vertices in the graph
		self.vertices = set()
		
	def addVertex(self, vertex):
		
		#if given vertex is already in the set, it prints
		if vertex in self.vertices:
			print("Vertex already exists.")
			
		#Otherwise it adds the vertex to the vertices set
		#As well as creating an index in the dictionary to store
		#adjacent vertices/edges
		else:
			self.vertices.add(vertex)
			self.vertexList[vertex] = set()
			print("Vertex added: %s" % vertex)
		
	def addEdge(self, edge1, edge2):
		#Checks to make sure vertices are in the graph. If not it prints
		if (edge1 not in self.vertices) or (edge2 not in self.vertices):
			print("One or more vertices not found.")
		#The next two statements are similar. For the first vertex,
		#It either creates an entry in vertexList to store the second
		#vertex or if one exists, just adds the second vertex.
		if (edge1 not in self.vertexList.keys()):
			self.vertexList[edge1] = set()
			self.vertexList[edge1].add(edge2)
		else:
			self.vertexList[edge1].add(edge2)
		
		#Similarly, this one adds the first edge to the second vertex's
		#set.
		if (edge2 not in self.vertexList.keys()):
			self.vertexList[edge1] = set()
			self.vertexList[edge1].add(edge1)
		else:
			self.vertexList[edge1].add(edge1)	
			
		print("Edge Added between: %s" % edge1,edge2)		
	
	def findVertex(self, value):
		#If the vertex given is not in the graph, it prints
		if value not in self.vertices:
			print("Vertex does not exist")
			
		#Otherwise it prints adjacent vertices.
		else:
			print("Vertex Found: %s" % value)
			print("Adjacent vertices: %s" % self.vertexList[value])
		
if __name__ == "__main__":
	graph = Graph()
	graph.addVertex(1)
	graph.addVertex(2)
	graph.addVertex(3)
	graph.addVertex(4)
	graph.addVertex(5)
	graph.addVertex(5)
	graph.addVertex(6)
	graph.addVertex(7)
	graph.addVertex(8)
	graph.addVertex(9)
	graph.addVertex(10)
	graph.addEdge(1,10)
	graph.addEdge(1,2)
	graph.addEdge(1,4)
	graph.addEdge(1,6)
	graph.addEdge(1,8)
	graph.addEdge(11,10)
	graph.addEdge(2,3)
	graph.addEdge(2,5)
	graph.addEdge(2,7)
	graph.addEdge(2,9)
	graph.addEdge(3,4)
	graph.addEdge(4,6)
	graph.addEdge(4,2)
	graph.addEdge(4,9)
	graph.addEdge(5,10)
	graph.addEdge(5,3)
	graph.addEdge(6,3)
	graph.addEdge(7,8)
	graph.addEdge(8,3)
	graph.addEdge(9,10)
	graph.addEdge(10,4)
	graph.findVertex(2)
	graph.findVertex(3)
	graph.findVertex(4)
	graph.findVertex(5)
	graph.findVertex(6)
