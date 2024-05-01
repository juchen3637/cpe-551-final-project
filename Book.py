# Author: Justin Chen
# Date: 4/30/2024
# Description: This file creates a class called Book that inherits from the Media class. The Book class takes in additional attributes such as authors, isbn, isbn13, languageCode, numPages, numRatings, pubDate, and publisher. The class has getter and setter methods for each attribute. The purpose of this class is to store information about books in a library catalog system.

from Media import Media

class Book(Media):
  """
  parameter 1: authors
  type: string
  parameter 2: isbn
  type: string
  parameter 3: isbn13
  type: string
  parameter 4: languageCode
  type: string
  parameter 5: numPages
  type: int
  parameter 6: numRatings
  type: int
  parameter 7: pubDate
  type: string
  parameter 8: publisher
  type: string
  """
  def __init__(self, id, title, authors, avgRating, isbn, isbn13, languageCode, numPages, numRatings, pubDate, publisher):
    super().__init__(id, title, avgRating)
    self.__authors = authors
    self.__isbn = isbn
    self.__isbn13 = isbn13
    self.__languageCode = languageCode
    self.__numPages = numPages
    self.__numRatings = numRatings
    self.__pubDate = pubDate
    self.__publisher = publisher
  
  def getAuthors(self):
    """
    The following are appropriate getter and setter methods for the Book class.
    """
    return self.__authors
  def getIsbn(self):
    return self.__isbn
  def getIsbn13(self):
    return self.__isbn13
  def getLanguageCode(self):
    return self.__languageCode
  def getNumPages(self):
    return self.__numPages
  def getNumRatings(self):
    return self.__numRatings
  def getPubDate(self):
    return self.__pubDate
  def getPublisher(self):
    return self.__publisher
  def setAuthors(self, authors):
    self.__authors = authors
  def setIsbn(self, isbn):
    self.__isbn = isbn
  def setIsbn13(self, isbn13):
    self.__isbn13 = isbn13
  def setLanguageCode(self, languageCode):
    self.__languageCode = languageCode
  def setNumPages(self, numPages):
    self.__numPages = numPages
  def setNumRatings(self, numRatings):
    self.__numRatings = numRatings
  def setPubDate(self, pubDate):
    self.__pubDate = pubDate
  def setPublisher(self, publisher):
    self.__publisher = publisher
