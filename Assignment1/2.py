class Queue:
	def __init__(self, size):
		self.size=size
		self.data=[0 for i in range(size)]
		self.front=-1
		self.rear=-1
	def insertion(self,item):
		if self.rear==self.size-1:
			print("Queue Overflow")
			return 0
		self.data[self.rear]=self.rear+1
		self.rear=self.rear+1
		if self.front==-1:
			self.front=0
		print(item,'inserted')
	def deletion(self):
		if self.front==-1 and self.rear==-1:
			print("Queue Underflow")
			return -1
		item=self.data[self.front]
		
		if self.front==-1 and self.rear==-1:
			self.front=self.front+1
		print(item,'deleted')
lq=Queue(3)
lq.insertion(5)
lq.insertion(3)
lq.insertion(2)
lq.insertion(0)
lq.deletion()
lq.deletion()

