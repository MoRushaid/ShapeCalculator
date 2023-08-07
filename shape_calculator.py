class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * (self.width + self.height)
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  def get_amount_inside(self, shape):
    a = shape.width
    b = shape.height
    return self.get_area() // (a*b)
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      row = '*' * self.width
      return (row + '\n') * self.height
  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)
  def __str__(self):
    return 'Square(side=' + str(self.width) + ')'
  
