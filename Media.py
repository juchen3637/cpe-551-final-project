class Media:
  def __init__(self, id, title, avgRating):
    self._id = id
    self._title = title
    self._avgRating = avgRating
  def getId(self):
    return self._id
  def getTitle(self):
    return self._title
  def getAvgRating(self):
    return self._avgRating
  def setId(self, id):
    self._id = id
  def setTitle(self, title):
    self._title = title
  def setAvgRating(self, avgRating):
    self._avgRating = avgRating

