class frequency:
  def __init__(self):
    self.str=str
    print("Enter the string to count the vowels:")
  def count(self):
    v='aeiouAEIOU'
    c=0
    for i in self.str:
      if i in v:
        c+=1
      print("No. of vowels are")
      c={i:self.str.count(i) for i in v if i in self.str}
      print("Frequency of each character in the string is",c)
  ob1=frequency()
  ob1.str=input()
  ob1.count()
      
