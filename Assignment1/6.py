class nameprint:
  def __init__(self,name):
    self.name=name
  def character(self):
    for i in range(0,5):
      print(self.name[i])
t=input("Enter your name:")
obj=nameprint(t)
obj.character()
