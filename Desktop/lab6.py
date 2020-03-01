class Node:
	def __init__(self,data):
		self.data = data
		self.nextPointer = None 


	def getData(self):
		return(self.data)
	def setData(Data):
		self.Data = data
	def getnextPointer(self):
		return(self.nextPointer)
	def setnextPointer(nextPointer):
		self.nextPointer = nextPointer

		
	class LinkedList:
	def__init__(self,head,size,tail):
		self.head  = head
		self.size = size 
		self.tail = tail
	def isEmpty():
		if(size == 0):
			return True
		return False 
	def addNode(newnode):
		if(isEmpty()):
			setHead(newnode)
		setTail(newnode)


	def setHead(newnode):
		self.head = newnode

	def setTail(newnode):
		self.tail.nextPointer = newnode
		self.tail = newnode 
	def getHead():
		return self.head
	def getTail():
		return self.tail 



