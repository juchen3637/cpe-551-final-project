# Author: Joseph Stefanoni
# Date: 4/30/2024
# Description: 
import Book
import Show
import Media
import os
import tkinter as tk
import tkinter.filedialog as fd

class Recommender:
  def __init__(self):
    self.__Books = dict() # Dictionary of Book Objects, where the book’s id is the key and the value is the object.
    self.__Shows = dict() # Dictionary of Show Objects, where the show’s id is the key and the value is the object.
    self.__Associations = dict() # Dictionary of dictionaries keeping track of association, where a show or book id is the key and the value is a dictionary.
      # For the inner dictionary, the key should be a show or book id and the value is the
      # number of times the outer id and inner id are associated.
    
  def loadBooks(self):
    file = ""
    while not os.path.exists(file):
      file = fd.askopenfilename(title="Book",initialdir=os.getcwd()) # Rename "Book" to title of GUI.
    with open(file, 'r') as lines:
      for line in lines:
        if line!=lines[0]:
          line = line.strip()
          info = list(line.split("\t"))
          # Book value: id, title, avgRating, authors, isbn, isbn13, languageCode, numPages, numRatings, pubDate, publisher
          self.__Books[info[0]] = Book(info)
          
  def loadShow(self):
    file = ""
    while not os.path.exists(file):
      file = fd.askopenfilename(title="Show",initialdir=os.getcwd()) # Rename "Show" to title of GUI.
    with open(file, 'r') as lines:
      for line in lines:
        if line!=lines[0]:
          line = line.strip()
          info = list(line.split("\t"))
          # Show value: id, type, title, directors, actors, avgRating, countryCode, dateAdded, year, rating, duration, genres, description
          self.__Shows[info[0]] = Show(info)
          
  def loadAssociations(self):
    file = ""
    while not os.path.exists(file):
      file = fd.askopenfilename(title="Show",initialdir=os.getcwd()) # Rename "Show" to title of GUI.
    with open(file, 'r') as lines:
      for line in lines:
        line = line.strip()
        info = list(line.split("\t")) # Size of 2
        if info[0] in self.__Associations.keys(): # Uses Show ID as Outer Dictionary Key
          if info[1] in self.__Associations[info[0]].keys():
            # OD: {Show ID, dict}, dict = OD[Show ID]
            # ID: {Book ID, val}, val = ID[Book ID] = OD[Show ID][Book ID]
            self.__Dicts[info[0]][info[1]] += 1
          else:
            self.__Dicts[info[0]][info[1]] = 1
        else:
          new_dict = dict()
          new_dict[info[1]] = 1 # Uses Book ID as Inner Dictionary Key
          self.__Associations[info[0]] = new_dict
        
        if info[1] in self.__Associations.keys(): # Uses Book ID as Outer Dictionary Key
          if info[0] in self.__Associations[info[1]].keys():
            # OD: {Book ID, dict}, dict = OD[Book ID]
            # ID: {Show ID, val}, val = ID[Show ID] = OD[Book ID][Show ID]
            self.__Dicts[info[1]][info[0]] += 1
          else:
            self.__Dicts[info[1]][info[0]] = 1
        else:
          new_dict = dict()
          new_dict[info[0]] = 1 # Uses Show ID as Inner Dictionary Key
          self.__Associations[info[1]] = new_dict
  
  def getMovieList(self):
    storage = ["Title", "Runtime"] # Contains all strings needed for output
    longestName = 0 # Used for finding max column space needed.
    for showInfo in self.__Shows.values():
      if showInfo.getType() == "Movie":  # If the show type is a movie.
        storage.append(showInfo.getTitle())
        storage.append(showInfo.getDuration())
        if len(showInfo.getTitle())>longestName:
          longestName = len(showInfo.getTitle())
    output = str()
    count = 0
    for i in storage:
      if count%2==0:
        output += f"{"\n" + i}" # Adds strings from storage using proper indenting
      else:
        output += f"{i :>{longestName+5}}" # Adds strings from storage using proper spacing
      count += 1
    return output
    
    