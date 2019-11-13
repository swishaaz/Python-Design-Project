import turtle
bob=turtle.Turtle()
turtle.bgcolor("black")

bob.color('white')
bob.speed(10)
bob.left(20)
for i in range(0,21,1):
  bob.left(10)
  for i in range(0,10,1):
    
      bob.forward(10)
      bob.left(10)
    
  bob.forward(90)
  bob.right(55)
  bob.backward(90)
  for i in range(0,10,1):
    
      bob.left(10)
      bob.backward(10)
    
  bob.backward(90)
