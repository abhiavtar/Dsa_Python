class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.list= [0 for i in range(size)]
        self.front = -1
        self.rear = -1

    def CQinsertion(self, item):
        if self.front==(self.rear+1)%self.size:
            print("Circular queue is full.")
        else:
            self.rear = (self.rear + 1) % self.size
            self.list[self.rear]=item
            if self.front==-1:
                self.front=0
                print("List of Circular Queue:",self.list)
    def traverse(self):
      if self.rear==self.front==-1:
          print("Circular queue is empty.")
      else:
        print("Circular queue:",self.list)
    def CQdeletion(self):
        if self.rear==self.front==-1:
          print("Circular queue is empty.")
          return
        item=self.list[self.front]
        if self.rear==self.front:
          self.rear=self.front=-1
        else:
          self.front=(self.front+1)%self.size
        return item
    s=circularQueue(5)
    s.CQinsertion(5)
    s.CQinsertion(15)
    s.CQinsertion(25)
    s.CQinsertion(50)
    s.CQinsertion(55)
    print("Deletion of an element:", s.CQdeletion())
    print("Deletion of an element:", s.CQdeletion())
    print("Deletion of an element:", s.CQdeletion())
    print("Deletion of an element:", s.CQdeletion())
    print("Deletion of an element:", s.CQdeletion())
    print("Circular Queue:", s.traverse())
