#Brandon Escamilla PSID: 1823960
# (1) Prompt the user to input a wall's height and width. Calculate and output the wall's area (integer).
import math

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
area = height * width

print("Wall area:", area, "square feet")

# (2) Extend to also calculate and output the amount of paint in gallons needed to paint the wall (floating point). Assume a gallon of paint covers 350 square feet. Store this value in a variable. Output the amount of paint needed using the %f conversion specifier.
paint = area / 350

print("Paint needed:", '{:.2f}'.format(paint), "gallons")

#(3) Extend to also calculate and output the number of 1 gallon cans needed to paint the wall. Hint: Use a math function to round up to the nearest gallon. (Submit for 2 points, so 6 points total).
cans = math.ceil(paint)
print("Cans needed:", cans, "can(s)\n")

#(4) Extend by prompting the user for a color they want to paint the walls. Calculate and output the total cost of the paint cans depending on which color is chosen. Hint: Use a dictionary to associate each paint color with its respective cost. Red paint costs $35 per gallon can, blue paint costs $25 per gallon can, and green paint costs $23 per gallon can. (Submit for 2 points, so 8 points total).
dict = {'red': 35, 'blue': 25, 'green': 23}
color = input("Choose a color to paint the wall:\n")
print("Cost of purchasing", color, "paint:", '${:.0f}'.format(cans * dict[color]))