# Author: Justin Chen
# Date: 4/30/2024
# Description: This file creates a class called Media that takes in an id, title, and average rating for a piece of media. The class has getter and setter methods for each attribute. The purpose of this class is to store information about media items in a library catalog system.

class Media:
  def __init__(self, id, title, avgRating):
    """
    parameter 1: id
    type: int
    parameter 2: title
    type: string
    parameter 3: avgRating
    type: float
    """
    self._id = id
    self._title = title
    self._avgRating = avgRating
  def getId(self):
    """
    The following are appropriate getter and setter methods for the Media class.
    """
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

