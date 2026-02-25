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
        # draw exactly h rows of characters with w columns
        # precompute horizontal border string and its length
        border = ("* " * w).rstrip()
        border_len = len(border)

        for row in range(h):
            if row == 0 or row == h - 1:
                # top or bottom row: asterisks separated by spaces
                print(border)
            else:
                # middle rows: left and right borders with interior spaces
                if w > 1:
                    # gap is total width minus two border asterisks
                    gap = border_len - 2
                    print("*" + " " * gap + "*")
                else:
                    print("*")
def main():
    print("="*50)
    print("Rectangle Calculator")
    print("="*50)

    while True:
        # get width with validation: only digits allowed
        while True:
            width_str = input("Enter the width of the rectangle: ").strip()
            if width_str.isdigit():
                width = int(width_str)
                break
            else:
                print("Please enter only digits (a positive integer) for the width.")
        # get height with validation: only digits allowed
        while True:
            height_str = input("Enter the height of the rectangle: ").strip()
            if height_str.isdigit():
                height = int(height_str)
                break
            else:
                print("Please enter only digits (a positive integer) for the height.")
        
        rect = Rectangle(width, height)
        
        print("="*50)
        print(f"Width: {rect.width}")
        print(f"Height: {rect.height}")
        print(f"Area: {rect.get_area()}")
        print(f"Perimeter: {rect.get_perimeter()}")
        print("="*50)
        print("\nGraphical representation:")
        rect.draw()
        print("="*50)

        # ask user whether to continue, only accept 'y' or 'n'
        while True:
            answer = input("\nCreate another rectangle? (y/n): ").strip().lower()
            if answer in ("y", "n"):
                break
            print("Please type 'y' for yes or 'n' for no.")
        if answer != "y":
            print("="*50)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
