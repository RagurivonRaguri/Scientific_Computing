import math  # Import pi

def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        area = math.pi * (dimension1 ** 2)
        return f"Area of the circle: {area:.2f}"
    
    elif shape == "rectangle":
        area = dimension1 * dimension2 
        return f"Area of the rectangle: {area:.2f}"
    
    elif shape == "triangle":
        area = 0.5 * dimension1 * dimension2 
        return f"Area of the triangle: {area:.2f}"
    
    else:
        return "Invalid shape! Please enter 'circle', 'rectangle', or 'triangle'."

print(calculate_area("circle", 5))  
print(calculate_area("rectangle", 10, 4))  
print(calculate_area("triangle", 6, 8)) 
print(calculate_area("hexagon", 7)) 
