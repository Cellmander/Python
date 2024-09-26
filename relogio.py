import turtle

tata = turtle.Turtle()
raio = 100

tata.circle(raio)
tata.left(90)
tata.up()
tata.forward(raio)
 
for i in range(12):
    tata.left(30)
    tata.forward(4*raio/5)
    tata.dot(5)
    tata.backward(4*raio/5)
    
tata.down()
tata.left(5)
tata.pencolor('red')
tata.forward(4*raio/5)
tata.backward(4*raio/5)

tata.left(45)
tata.pencolor('black')
tata.forward(2*raio/5)
tata.backward(2*raio/5)

tata.right(130)
tata.forward(3*raio/5)
tata.backward(3*raio/5)

