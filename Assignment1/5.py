class sucessiveCharacter:
  def __init__(self):
    self.string=string
  def repetition(self):
    r=self.string[0]
    for i in range(1,len(self.string)):
      if self.string[i]==self.string[i-1]:
        r+='*'
      else:
        r+=self.string[i]
    print("The new string is",r)
c=input("Enter a string:")
obj=sucessiveCharacter(c)
obj.repetition()
