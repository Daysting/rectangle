# Erick Hofer
#CIS261
# Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
def main():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    
    rect = Rectangle(width, height)
    
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")

if __name__ == "__main__":
    main()
