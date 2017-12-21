class Person:
  def __init__(self,id):
    self.id = id;
    print("constructor")
  def __del__(self):
    print(self.id,"object destroyed")
  def setname(self,fname,lname):
    self.fname = fname
    self.lname = lname
  def printname(self):
    print(self.fname," ",self.lname)


personName = Person(5)
personName.setname("jagruti","bhudiya")
personName.printname()
personName.__del__()

