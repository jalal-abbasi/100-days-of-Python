# from turtle import Turtle, Screen
#
# my_turtle = Turtle()
# my_turtle.color("DarkOliveGreen3")
# my_turtle.shape("turtle")
#
# my_turtle.forward(100)
#
# screen = Screen()
# screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokeman Name", ["Pilachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)
