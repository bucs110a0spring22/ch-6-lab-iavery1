
import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
      count += 1
      if (n % 2) == 0:        # n is even
        n = n // 2
      else:                   # n is odd
        n = n * 3 + 1
    return count              # the last print is 1

def lineGraph(uplim):
  screen = turtle.Screen()
  y_maximum = 0
  for count in range(uplim):
    y_new = seq3np1(count+1)
    if y_new > y_maximum:
      y_maximum = y_new
  screen.setworldcoordinates(0,0,uplim + 10, y_maximum + 2)
  screen.bgcolor("lightblue")
  myturtle = turtle.Turtle()
  myturtle.speed(0)
  myturtle.fillcolor("green")
  max_so_far = 0
  for start in range (uplim):
    y_coordinate = seq3np1(start + 1)
    if max_so_far < y_coordinate:
      max_so_far = y_coordinate
    myturtle.goto(start + 1, y_coordinate)
    result = "Maximum so far: " +str(start + 1) + ", " + str(max_so_far)
    print(result)
  screen.exitonclick()

def main():
  uplim = int(input("Please enter the upper bound: "))
  lineGraph(uplim)
  if (uplim > 0):
    for start in range (uplim):
      value = int(seq3np1(start + 1))
      print("The starting value is " + str(start + 1) + ", and the number of iterations is " + str(value))
  else:
    print("Invalid value")
main()
