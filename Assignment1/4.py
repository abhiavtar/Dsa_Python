class series:
  def __init__(self,num):
    self.num=num
  def seriessum(self):
    s=0
    for i in range(n+1):
      s=s+i
    print("Sum of the series:",s)
n=int(input("Enter the value of n: "))
a=series(n)
a.seriessum()
