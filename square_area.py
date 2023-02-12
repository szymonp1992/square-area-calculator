# START THE NEXT LEARNING BLOCK BY WRITING AN ERROR PRONE VERSION OF THIS


def triangle_area(a, h):
    area = (a*h)/2
    return area

def rectangle_area(a, b):
    area = a*b
    return area

def circle_area(r):
    PI = 3.14
    area = PI * pow(r, 2)
    return area

def main():

    while True:
        shape = input("What is your shape? Triangle, rectangle or circle? ")
        if shape.lower() != "triangle" and shape.lower() != "rectangle" and shape.lower() != "circle":
            print(f'{shape} is not one of the shapes you can use in this app. Please try again')
            continue
        else:
            break

    if shape.lower() == "triangle":
        while True:
            try:
                triangle_a = int(input("What is your triangle's base length (in cm)? "))
                triangle_h = int(input("What is your triangle's height (in cm)? "))
                tri_area = triangle_area(triangle_a, triangle_h)
                print(f"The triangle square area is {tri_area} cm2")
                break
            except:
                print('You did not provide valid data')
    
    elif shape.lower() == "rectangle":
        while True:
            try:
                rectangle_a = int(input("What is your rectangle's base length (in cm)? "))
                rectangle_b = int(input("What is your rectangle's side length (in cm)? "))
                rec_area = rectangle_area(rectangle_a, rectangle_b)
                print(f"The rectangle square area is {rec_area} cm2")
                break
            except:
                print('You did not provide valid data')
    elif shape.lower() == "circle":
        while True:
            try:
                circle_r = int(input("What is your circle's radius (in cm)? "))
                cir_area = circle_area(circle_r)
                print(f"The circle square area is {cir_area} cm2")
            except:
                print('You did not provide valid data. Try again')

main()