class Parent:
  val1 = "this is val 1"
  val2 = "this is val 2"

class child(Parent):
  pass

parent_ = Parent()
print(parent_.val1)
print(parent_.val2)

child_ = child()
print(child_.val1)
print(child_.val2)
  

  
