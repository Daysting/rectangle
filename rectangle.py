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
    
    def draw(self):
        """Print a text graphic of the rectangle border using asterisks.
        Only the outer edge is drawn; interior is spaces. Dimensions are
        truncated to integers for drawing.
        """
        w = int(self.width)
        h = int(self.height)
        if w <= 0 or h <= 0:
            print("Cannot draw a rectangle with non‑positive dimensions.")
            return
        # compute number of interior gaps; use the larger of the horizontal
        # and vertical counts so the spacing between the vertical “lines”
        # matches the spacing between the horizontal ones
        interior = max(w - 2, h - 2, 0)
        # build a border that has a space between every asterisk
        border = ("* " * w).rstrip()
        # width in characters for interior calculation
        interior_gap = len(border) - 2 if w > 1 else 0
        # top border
        print(border)
        # middle rows – may be taller than input height when width > height
        for _ in range(interior):
            if w > 1:
                print("*" + " " * interior_gap + "*")
            else:
                print("*")
        # bottom border
        if h > 1:
            print(border)
def main():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    
    rect = Rectangle(width, height)
    
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")
    print("\nGraphical representation:")
    rect.draw()

if __name__ == "__main__":
    main()
