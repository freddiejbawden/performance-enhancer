class IDGenerator:
  
  def __init__(self, begin):
    self.current = begin - 1

  def next(self):
    self.current += 1
    return self.current
