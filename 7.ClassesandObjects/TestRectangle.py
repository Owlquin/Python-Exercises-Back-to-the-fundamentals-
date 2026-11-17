from Rectangle import Rectangle

def main():
    rectangle1 = Rectangle(4,40)
    rectangle2 = Rectangle(3.5,35.7)

    print(f"Width of rectangle1: {rectangle1.width}, Height of rectangle1: {rectangle1.height}")
    print(f"Area of rectangle1: {rectangle1.getArea()}, Perimeter of rectangle1: {rectangle1.getPerimeter()}")

    print(f"Width of rectangle2: {rectangle2.width}, Height of rectangle2: {rectangle2.height}")
    print(f"Area of rectangle2: {rectangle2.getArea()}, Perimeter of rectangle2: {rectangle2.getPerimeter()}")

main()