# Author: Justin Chen
# Date: 4/30/2024
# Description: This file creates a class called Show that inherits from the Media class. The Show class takes in additional attributes such as type, directors, actors, countryCode, dateAdded, year, rating, duration, genres, and description. The class has getter and setter methods for each attribute. The purpose of this class is to store information about TV shows in a library catalog system.

from Media import Media

class Show(Media):
  def __init__(self, id, type, title, directors, actors, avgRating, countryCode, dateAdded, year, rating, duration, genres, description):
    """
    parameter 1: type
    type: string
    parameter 2: directors
    type: string
    parameter 3: actors
    type: string
    parameter 4: countryCode
    type: string
    parameter 5: dateAdded
    type: string
    parameter 6: year
    type: int
    parameter 7: rating
    type: float
    parameter 8: duration
    type: float
    parameter 9: genres
    type: string
    parameter 10: description
    type: string
    """
    super().__init__(id, title, avgRating)
    self.__type = type
    self.__directors = directors
    self.__actors = actors
    self.__countryCode = countryCode
    self.__dateAdded = dateAdded
    self.__year = year
    self.__rating = rating
    self.__duration = duration
    self.__genres = genres
    self.__description = description
  def getType(self):
    """
    The following are appropriate getter and setter methods for the Show class.
    """
    return self.__type
  def getDirectors(self):
    return self.__directors
  def getActors(self):
    return self.__actors
  def getCountryCode(self):
    return self.__countryCode
  def getDateAdded(self):
    return self.__dateAdded
  def getYear(self):
    return self.__year
  def getRating(self):
    return self.__rating
  def getDuration(self):
    return self.__duration
  def getGenres(self):
    return self.__genres
  def getDescription(self):
    return self.__description
  def setType(self, type):
    self.__type = type
  def setDirectors(self, directors):
    self.__directors = directors
  def setActors(self, actors):
    self.__actors = actors
  def setCountryCode(self, countryCode):
    self.__countryCode = countryCode
  def setDateAdded(self, dateAdded):
    self.__dateAdded = dateAdded
  def setYear(self, year):
    self.__year = year
  def setRating(self, rating):
    self.__rating = rating
  def setDuration(self, duration):
    self.__duration = duration
  def setGenres(self, genres):
    self.__genres = genres
  def setDescription(self, description):
    self.__description = description
  
