class Stack:
	def __init__(self,size):
		self.size=size
		self.data=[0 for i in range(size)]
		self.top=-1
	def Push(self, item):
		if self.top==self.size-1:
			print("Stack Overflow")
			return 0
		self.top=self.top+1
		self.data[self.top]=item
		print(item, 'pushed')
	def Pop(self):
		if self.top==-1:
			print("Stack Underflow")
			return -1
		item=self.data[self.top]
		self.top=self.top-1
		print(item, 'popped')
st=Stack(3)
st.Push(4)
st.Push(7)
st.Push(3)
st.Push(9)
(st.Pop())
(st.Pop())
(st.Pop())
(st.Pop())
