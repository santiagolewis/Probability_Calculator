import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      color = key
      num = value
      while num > 0:
        self.contents.append(color)   
        num -= 1

    self.contents_copy = self.contents.copy()

  def draw(self, number):
    #I restaured the contents list every time the draw method is used. Otherwise the list would be changed because later we will remove some items on it and that is going to modify the original contents list.
    self.contents = self.contents_copy.copy()
    if len(self.contents) >= number:
      rand = random.sample(self.contents, number)
      for x in rand:
        self.contents.remove(x)
      return rand
    else:
      return self.contents
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count_2 = 0
  for exper in range(num_experiments):
    count = 0
    dra = hat.draw(num_balls_drawn)
    dicti = {}
    for ball in dra:
      dicti[ball] = 0
    for ball in dra:
      dicti[ball] += 1

    #Here i checked if every key, value pair in the 'dicti' dictionary is at least equal to the key, value pair in the 'expected_balls' dictionary. If so, we add 1 to 'count'. Finally if 'count' is equal to len(expected_balls) it means that every item in 'dicti' is at least equal to it's value in expected_balls, in which case we add 1 to 'count_2'.
    for key, val in dicti.items():
      try:
        if val >= expected_balls[key]:
          count += 1
      except KeyError:
        continue
    if count == len(expected_balls):
      count_2 += 1
  probability = count_2 / num_experiments
  return probability
