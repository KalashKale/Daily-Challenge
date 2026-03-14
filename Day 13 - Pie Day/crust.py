import math
def cut_pie(diameter, friends):
  circumference = math.pi * diameter
  return round((circumference / friends), 2)