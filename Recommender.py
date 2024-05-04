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
  
  def getTVList(self):
    storage = ["Title", "Seasons"] # Contains all strings needed for output
    longestName = 0 # Used for finding max column space needed.
    for showInfo in self.__Shows.values():
      if showInfo.getType() == "TV Show":  # If the show type is a TV show.
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
  
  def getBookList(self):
    storage = ["Title", "Author(s)"] # Contains all strings needed for output
    longestName = 0 # Used for finding max column space needed.
    for bookInfo in self.__Books.values():
      storage.append(bookInfo.getTitle())
      storage.append(bookInfo.getAuthors())
      if len(bookInfo.getTitle())>longestName:
        longestName = len(bookInfo.getTitle())
    output = str()
    count = 0
    for i in storage:
      if count%2==0:
        output += f"{"\n" + i}" # Adds strings from storage using proper indenting
      else:
        output += f"{i :>{longestName+5}}" # Adds strings from storage using proper spacing
      count += 1
    return output
  
  def getMovieStats(self):
    ratingPercents = dict() # {"16+":0, "ALL":0, "PG":0, "R":0, "18+":0, "14+":0, "7+":0}
    avgMovieDuration = 0
    movieCount = 0
    directorCounts = dict()
    actorCounts = dict()
    genreCounts = dict()
    for movieInfo in self.__Shows.values():
      if movieInfo.getType() == "Movie":  # If the show type is a movie.
        # Getting Rating Percentages
        if movieInfo.getRating() in ratingPercents.keys():
          ratingPercents[movieInfo.getRating()] += 1
        else:
          ratingPercents[movieInfo.getRating()] = 1
        # Getting Average Movie Duration
        avgMovieDuration += int(movieInfo.getDuration()[:-4]) # Remove last 4 characters which is " min".
        movieCount += 1
        # Getting Top Movie Director
        directors_str = movieInfo.getDirectors()
        directors_str = directors_str.strip()
        directors_list = list(directors_str.split("\\"))
        for director in directors_list:
          if director in directorCounts.keys():
            directorCounts[director] += 1
          else:
            directorCounts[director] = 1
        # Getting Top Movie Actor
        actors_str = movieInfo.getActors()
        actors_str = actors_str.strip()
        actors_list = list(actors_str.split("\\"))
        for actor in actors_list:
          if actor in actorCounts.keys():
            actorCounts[actor] += 1
          else:
            actorCounts[actor] = 1
        # Getting Most Frequent Movie Genre
        genres_str = movieInfo.getGenres()
        genres_str = genres_str.strip()
        genres_list = list(genres_str.split("\\"))
        for genre in genres_list:
          if genre in genreCounts.keys():
            genreCounts[genre] += 1
          else:
            genreCounts[genre] = 1
    # Getting Rating Percentages
    totalRating = 0
    for count in ratingPercents.values():
      totalRating += count
    for key in ratingPercents.keys():
      ratingPercents[key] = float(f"{ratingPercents[key] / totalRating :.2f}") # Turns each rating total into a percentage given the total of all ratings.
    # Getting Average Movie Duration
    avgMovieDuration = float(f"{avgMovieDuration / movieCount :.2f}")
    # Getting Director who directed the most movies
    maxMoviesDirected = max(directorCounts.values())
    topDirector = ""
    for director in directorCounts.keys():
      if directorCounts[director] == maxMoviesDirected:
        if topDirector=="": # In case there are multiple top directors
          topDirector += director
        else:
          topDirector += "\\" + director
    # Getting Actor who acted in the most movies
    maxMoviesActedIn = max(actorCounts.values())
    topActor = ""
    for actor in actorCounts.keys():
      if actorCounts[actor] == maxMoviesActedIn:
        if topActor=="": # In case there are multiple top actors
          topActor += actor
        else:
          topActor += "\\" + actor
    # Getting most frequent movie genre
    maxMoviesGenre = max(genreCounts.values())
    topGenre = ""
    for genre in genreCounts.keys():
      if genreCounts[genre] == maxMoviesGenre:
        if topGenre=="": # In case there are multiple top genres
          topGenre += genre
        else:
          topGenre += "\\" + genre
    return ratingPercents, avgMovieDuration, topDirector, topActor, topGenre
  
  def getTVStats(self):
    ratingPercents = dict()
    avgSeasonsNum = 0
    showCount = 0
    actorCounts = dict()
    genreCounts = dict()
    for showInfo in self.__Shows.values():
      if showInfo.getType() == "TV Show":  # If the show type is a TV Show.
        # Getting Rating Percentages
        if showInfo.getRating() in ratingPercents.keys():
          ratingPercents[showInfo.getRating()] += 1
        else:
          ratingPercents[showInfo.getRating()] = 1
        # Getting Average number of Seasons
        avgSeasonsNum += int(showInfo.getDuration()[:-7]) # Remove last 7 characters which is either "seasons" or " season". The integer removes the leftover space in seasons.
        showCount += 1
        # Getting Top Movie Actor
        actors_str = showInfo.getActors()
        actors_str = actors_str.strip()
        actors_list = list(actors_str.split("\\"))
        for actor in actors_list:
          if actor in actorCounts.keys():
            actorCounts[actor] += 1
          else:
            actorCounts[actor] = 1
        # Getting Most Frequent Movie Genre
        genres_str = showInfo.getGenres()
        genres_str = genres_str.strip()
        genres_list = list(genres_str.split("\\"))
        for genre in genres_list:
          if genre in genreCounts.keys():
            genreCounts[genre] += 1
          else:
            genreCounts[genre] = 1
    # Getting Rating Percentages
    totalRating = 0
    for count in ratingPercents.values():
      totalRating += count
    for key in ratingPercents.keys():
      ratingPercents[key] = float(f"{ratingPercents[key] / totalRating :.2f}") # Turns each rating total into a percentage given the total of all ratings.
    # Getting Average number of Seasons
    avgSeasonsNum = float(f"{avgSeasonsNum / showCount :.2f}")
    # Getting Actor who acted in the most TV Shows
    maxShowsActedIn = max(actorCounts.values())
    topActor = ""
    for actor in actorCounts.keys():
      if actorCounts[actor] == maxShowsActedIn:
        if topActor=="": # In case there are multiple top actors
          topActor += actor
        else:
          topActor += "\\" + actor
    # Getting most frequent TV Show genre
    maxShowsGenre = max(genreCounts.values())
    topGenre = ""
    for genre in genreCounts.keys():
      if genreCounts[genre] == maxShowsGenre:
        if topGenre=="": # In case there are multiple top genres
          topGenre += genre
        else:
          topGenre += "\\" + genre
    return ratingPercents, avgSeasonsNum, topActor, topGenre
    
    