import turtle
t=turtle.Turtle()
count=0

angle = 30

# Set initial distance
distance = 1

# Set the number of iterations
iterations = 100

# Draw the spiral helix pattern
for _ in range(iterations):
    t.forward(distance)
    t.left(angle)
    distance += 1

# Keep the window open
turtle.done()

