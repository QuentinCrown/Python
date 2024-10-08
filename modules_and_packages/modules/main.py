from math_operations import calculator
from math_operations import geometry


add_result = calculator.add(5, 3)
print("Addition result:", add_result)

subtract_result = calculator.subtract(10, 4)
print("Subtraction result:", subtract_result)

rectangle_result = geometry.rectangle_area(5, 4)
print("Rectangle area:", rectangle_result)

triangle_result = geometry.triangle_area(6, 3)
print("Triangle area:", triangle_result)

circle_result = geometry.circle_area(7)
print("Circle area:", circle_result)
