import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for x in range(value):
        self.contents.append(key)

  def draw(self, num_balls_drawn):
    if num_balls_drawn >= len(self.contents):
      return self.contents
      
    if num_balls_drawn <= len(self.contents):
      balls_drawn = []
      for d in range(num_balls_drawn):
        rand_balls = random.randrange(len(self.contents))
        balls_drawn.append(self.contents[rand_balls])
        self.contents.pop(rand_balls)
      return balls_drawn
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  contents = copy.deepcopy(hat.contents)
  count = 0
  expected = []  
  
  for key, value in expected_balls.items():
    for i in range(value):
      expected.append(key)
      
  for num in range(num_experiments):
    match = 0
    hat.contents = copy.deepcopy(contents)
    drawn = hat.draw(num_balls_drawn)

    for x in expected:
      for y in drawn:
        if x == y:
          match += 1
          drawn.pop(drawn.index(x))
          break
          
      if match == len(expected):
        count += 1

  return count/num_experiments

    
    

  
  
  
