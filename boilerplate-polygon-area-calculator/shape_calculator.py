class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, set):
    self.width = set

  def set_height(self, set):
    self.height = set
    
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (self.width + self.height) * 2

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return ("Too big for picture.")
    else:
      return ((("*" * self.width)+ "\n") * self.height)

  def __str__(self):
    return ("Rectangle(width={0}, height={1})").format(self.width, self.height)

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    
  def set_side(self, set):
    self.set_width(set)
    self.set_height(set)

  def __str__(self):
    return (("Square(side={0})").format(self.width))

