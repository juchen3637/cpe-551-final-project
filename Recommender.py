# Author: Joseph Stefanoni
# Date: 4/30/2024 - 5/4/24
# Description: Recommender Class which can load books, movies, and associations (all .csv files),
#              can get a list of the TV shows, movies, or books, can get book, TV, or Movie stats,
#              can search Books or TV and Movies by title, and can get recommendations of books given
#              a TV show or movie title, or can get recommendations of shows and movies given a book title.
import Book
import Show
import os
import tkinter
import tkinter.filedialog as fd
import tkinter.messagebox as mb

class Recommender:
  def __init__(self):
    self.__Books = dict() # Dictionary of Book Objects, where the book’s id is the key and the value is the object.
    self.__Shows = dict() # Dictionary of Show Objects, where the show’s id is the key and the value is the object.
    self.__Associations = dict() # Dictionary of dictionaries keeping track of association, where a show or book id is the key and the value is a dictionary.
      # For the inner dictionary, the key should be a show or book id and the value is the
      # number of times the outer id and inner id are associated.
    
  def loadBooks(self):
    """Loads all of the data from a selected book file using an askopenfilename dialog.
    """
    file = ""
    while not os.path.exists(file):
      file = fd.askopenfilename(title="Select book file to load",initialdir=os.getcwd()) # Rename "Book" to title of GUI.
    with open(file, 'r') as lines:
      for line in lines:
        if line[0:4]!="book":
          line = line.strip()
          info = list(line.split(","))
          # Book value: id, title, avgRating, authors, isbn, isbn13, languageCode, numPages, numRatings, pubDate, publisher
          self.__Books[info[0]] = Book.Book(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10])
          
  def loadShows(self):
    """Loads all of the data from a selected show file using an askopenfilename dialog.
    """
    file = ""
    while not os.path.exists(file):
      file = fd.askopenfilename(title="Select show file to load",initialdir=os.getcwd()) # Rename "Show" to title of GUI.
    with open(file, 'r') as lines:
      for line in lines:
        if line[0:4]!="show":
          line = line.strip()
          info = list(line.split(","))
          # Show value: id, type, title, directors, actors, avgRating, countryCode, dateAdded, year, rating, duration, genres, description
          self.__Shows[info[0]] = Show.Show(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10], info[11], info[12])
          
  def loadAssociations(self):
    """Loads all of the data from a selected association file using an askopenfilename dialog.
    """
    file = ""
    while not os.path.exists(file):
      file = fd.askopenfilename(title="Select associations file to load",initialdir=os.getcwd()) # Rename "Show" to title of GUI.
    with open(file, 'r') as lines:
      for line in lines:
        line = line.strip()
        info = list(line.split(",")) # Size of 2
        if info[0] in self.__Associations.keys(): # Uses Show ID as Outer Dictionary Key
          if info[1] in self.__Associations[info[0]].keys():
            # OD: {Show ID, dict}, dict = OD[Show ID]
            # ID: {Book ID, val}, val = ID[Book ID] = OD[Show ID][Book ID]
            self.__Associations[info[0]][info[1]] += 1
          else:
            self.__Associations[info[0]][info[1]] = 1
        else:
          new_dict = dict()
          new_dict[info[1]] = 1 # Uses Book ID as Inner Dictionary Key
          self.__Associations[info[0]] = new_dict
        
        if info[1] in self.__Associations.keys(): # Uses Book ID as Outer Dictionary Key
          if info[0] in self.__Associations[info[1]].keys():
            # OD: {Book ID, dict}, dict = OD[Book ID]
            # ID: {Show ID, val}, val = ID[Show ID] = OD[Book ID][Show ID]
            self.__Associations[info[1]][info[0]] += 1
          else:
            self.__Associations[info[1]][info[0]] = 1
        else:
          new_dict = dict()
          new_dict[info[0]] = 1 # Uses Show ID as Inner Dictionary Key
          self.__Associations[info[1]] = new_dict
  
  def getMovieList(self):
    """Returns the Title and Runtime for all of the stored movies with proper headers and column spacings.

    Returns:
        str: Title and Runtime of all of the stored movies with proper headers and column spacings.
    """
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
        output += f"\n{i}" + " "*(longestName+4-len(i)) # Adds strings from storage using proper indenting
      else:
        output += f"{i}" # Adds strings from storage using proper spacing
      count += 1
    return output
  
  def getTVList(self):
    """Returns the Title and Seasons for all of the stored TV Shows with proper headers and column spacings.

    Returns:
        str: Title and Seasons of all of the stored TV Shows with proper headers and column spacings.
    """
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
        output += f"\n{i}" + " "*(longestName+4-len(i)) # Adds strings from storage using proper indenting
      else:
        output += f"{i}" # Adds strings from storage using proper spacing
      count += 1
    return output
  
  def getBookList(self):
    """Returns the Title and Authors for all of the stored books with proper headers and column spacings.
    
    Returns:
        str: Title and Authors of all of the stored books with proper headers and column spacings.
    """
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
        output += f"\n{i}" + " "*(longestName+4-len(i)) # Adds strings from storage using proper indenting
      else:
        output += f"{i}" # Adds strings from storage using proper spacing
      count += 1
    return output
  
  def getMovieStats(self):
    """Returns the statistics regarding movies.
    
    Returns:
        dict (ratingPercents): Keys are rating names and values are the corresponding percentages compared to the total ratings.
        float (avgMovieDuration): Average Movie Duration.
        str (topDirector): Name of Director who directed the most movies.
        str (topActor): Name of Actor who acted in the most movies.
        str (topGenre): Name of Genre in the most movies.
    """
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
          if director!="":
            if director in directorCounts.keys():
              directorCounts[director] += 1
            else:
              directorCounts[director] = 1
        # Getting Top Movie Actor
        actors_str = movieInfo.getActors()
        actors_str = actors_str.strip()
        actors_list = list(actors_str.split("\\"))
        for actor in actors_list:
          if actor!="":
            if actor in actorCounts.keys():
              actorCounts[actor] += 1
            else:
              actorCounts[actor] = 1
        # Getting Most Frequent Movie Genre
        genres_str = movieInfo.getGenres()
        genres_str = genres_str.strip()
        genres_list = list(genres_str.split("\\"))
        for genre in genres_list:
          if genre!="":
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
        # if topDirector=="": # In case there are multiple top directors
        #   topDirector += director
        # else:
        #   topDirector += "\\" + director
        topDirector = director
        break
    # Getting Actor who acted in the most movies
    maxMoviesActedIn = max(actorCounts.values())
    topActor = ""
    for actor in actorCounts.keys():
      if actorCounts[actor] == maxMoviesActedIn:
        # if topActor=="": # In case there are multiple top actors
        #   topActor += actor
        # else:
        #   topActor += "\\" + actor
        topActor = actor
        break
    # Getting most frequent movie genre
    maxMoviesGenre = max(genreCounts.values())
    topGenre = ""
    for genre in genreCounts.keys():
      if genreCounts[genre] == maxMoviesGenre:
        # if topGenre=="": # In case there are multiple top genres
        #   topGenre += genre
        # else:
        #   topGenre += "\\" + genre
        topGenre = genre
        break
    return ratingPercents, avgMovieDuration, topDirector, topActor, topGenre
  
  def getTVStats(self):
    """Returns the statistics regarding TV Shows.
    
    Returns:
        dict (ratingPercents): Keys are rating names and values are the corresponding percentages compared to the total ratings.
        float (avgSeasonNum): Average number of TV Show Seasons.
        str (topActor): Name of Actor who acted in the most tv shows.
        str (topGenre): Name of Genre in the most tv shows.
    """
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
          if actor!="":
            if actor in actorCounts.keys():
              actorCounts[actor] += 1
            else:
              actorCounts[actor] = 1
        # Getting Most Frequent Movie Genre
        genres_str = showInfo.getGenres()
        genres_str = genres_str.strip()
        genres_list = list(genres_str.split("\\"))
        for genre in genres_list:
          if genre!="":
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
        # if topActor=="": # In case there are multiple top actors
        #   topActor += actor
        # else:
        #   topActor += "\\" + actor
        topActor = actor
        break
    # Getting most frequent TV Show genre
    maxShowsGenre = max(genreCounts.values())
    topGenre = ""
    for genre in genreCounts.keys():
      if genreCounts[genre] == maxShowsGenre:
        # if topGenre=="": # In case there are multiple top genres
        #   topGenre += genre
        # else:
        #   topGenre += "\\" + genre
        topGenre = genre
        break
    return ratingPercents, avgSeasonsNum, topActor, topGenre
  
  def getBookStats(self):
    """Returns the statistics regarding books.
    
    Returns:
        float (avgPageCounts): Average number of pages between all the books.
        str (topAuthor): Name of Author who wrote the most books.
        str (topPublisher): Name of Publisher who published the most books.
    """
    avgPageCounts = 0
    bookCount = 0
    authorCounts = dict()
    publisherCounts = dict()
    for bookInfo in self.__Books.values():
      # Getting Average Page Numbers
      avgPageCounts += int(bookInfo.getNumPages()) # Remove last 7 characters which is either "seasons" or " season". The integer removes the leftover space in seasons.
      bookCount += 1
      # Getting the Author(s) who wrote the most books
      authors_str = bookInfo.getAuthors()
      authors_str = authors_str.strip()
      authors_list = list(authors_str.split("\\"))
      for author in authors_list:
        if author!="":
          if author in authorCounts.keys():
            authorCounts[author] += 1
          else:
            authorCounts[author] = 1
      # Getting the Publisher who published the most books
      publishers_str = bookInfo.getPublishers()
      publishers_str = publishers_str.strip()
      publishers_list = list(publishers_str.split("\\"))
      for publisher in publishers_list:
        if publisher!="":
          if publisher in publisherCounts.keys():
            publisherCounts[publisher] += 1
          else:
            publisherCounts[publisher] = 1
    # Getting Average number of pages
    avgPageCounts = float(f"{avgPageCounts / bookCount :.2f}")
    # Getting the Author(s) who wrote the most books
    maxBooksWrote = max(authorCounts.values())
    topAuthor = ""
    for author in authorCounts.keys():
      if authorCounts[author] == maxBooksWrote:
        # if topAuthor=="": # In case there are multiple top authors
        #   topAuthor += author
        # else:
        #   topAuthor += "\\" + author
        topAuthor = author
        break
    # Getting most frequent TV Show genre
    maxBooksPublished = max(publisherCounts.values())
    topPublisher = ""
    for publisher in publisherCounts.keys():
      if publisherCounts[publisher] == maxBooksPublished:
        # if topPublisher=="": # In case there are multiple top genres
        #   topPublisher += publisher
        # else:
        #   topPublisher += "\\" + publisher
        topPublisher = publisher
        break
    return avgPageCounts, topAuthor, topPublisher
  
  def searchTVMovies(self, media, title, director, actor, genre):
    """Takes in strings representing a movie or tv show, a title, a director, an actor,
       and a genre, and returns information regarding Movies or TV Shows.

    Args:
        media (str): string representing media type (whether its a TV Show or Movie)
        title (str): Title of said media.
        director (str): Name of the desired media's director.
        actor (str): Name of the desired actor in the media.
        genre (str): Name of the desired media's genre.

    Returns:
        str: All corresponding Shows/Movies with the related inputs displaying neatly with appropriate headers and column spacing.
    """
    if media!="TV Show" and media!="Movie":
      mb.showerror(title="Error", message=f"Select Movie or TV Show from Type first.")
      return "No Results"
    if title=="" and director=="" and actor=="" and genre=="":
      mb.showerror(title="Error", message=f"Enter information for the Title, Directory, Actor and/or Genre first.")
      return "No Results"
    mediaList = ["Title", "Director", "Actors", "Genre"] # Contains all strings needed for output.
    ShowObjectsList = list() # Contains all Show objects needed.
    columnLengths = [5, 8, 6, 5] # Desired Column Lengths for each column for proper display.
    flags = [1, 1, 1, 1] # Boolean flags for checking if an input is blank.
    if title=="":
      flags[0] = 0 # Any flag set to 0 will not be used in the matching process.
    if director=="":
      flags[1] = 0
    if actor=="":
      flags[2] = 0
    if genre=="":
      flags[3] = 0
    for showInfo in self.__Shows.values():
      if media==showInfo.getType(): # If the types match, add the object to the media list.
        showIsMatch = True
        if flags[0]==1 and title!=showInfo.getTitle(): # If there is a title inputted and it doesn't match, do not add show.
          showIsMatch = False
        if flags[1]==1 and director!=showInfo.getDirectors(): # If there is a director inputted and it doesn't match, do not add show.
          showIsMatch = False
        if flags[2]==1: # If there is an actor inputted and it doesn't match, don't add show.
          actors_str = showInfo.getActors()
          actors_str = actors_str.strip()
          actors = list(actors_str.split("\\"))
          actorFlag = False
          for person in actors: # Check if the inputted actor's name is in the list of actors
            if actor==person:
              actorFlag = True
          if not actorFlag:
            showIsMatch = False
        if flags[3]==1: # If there is a genre inputted and it doesn't match, don't add show.
          genres_str = showInfo.getGenres()
          genres_str = genres_str.strip()
          genres = list(genres_str.split("\\"))
          genreFlag = False
          for showGenre in genres: # Check if the inputted genre is in the list of genres
            if genre==showGenre:
              genreFlag = True
          if not genreFlag:
            showIsMatch = False
        if showIsMatch: # If everything matched, show is added.
          ShowObjectsList.append(showInfo) 
    for show in ShowObjectsList:
      if len(show.getTitle())>columnLengths[0]:
        columnLengths[0] = len(show.getTitle())
      if len(show.getDirectors())>columnLengths[1]:
        columnLengths[1] = len(show.getDirectors())
      if len(show.getActors())>columnLengths[2]:
        columnLengths[2] = len(show.getActors())
      if len(show.getGenres())>columnLengths[3]:
        columnLengths[3] = len(show.getGenres())
      mediaList.append(show.getTitle())
      mediaList.append(show.getDirectors())
      mediaList.append(show.getActors())
      mediaList.append(show.getGenres())
    output = str()
    count = 0
    for i in mediaList:
      if count%4==0:
        output += f"\n{i}" + " "*(columnLengths[0]+4-len(i)) # Adds strings from the mediaList using proper indenting
      elif count%4==3:
        output += f"{i}" # Adds strings 
      else:
        output += f"{i}" + " "*(columnLengths[count%4]+4-len(i)) # Adds strings from mediaList using proper spacing
      count += 1
    return output
    
  def searchBooks(self, title, author, publisher):
    """Takes in strings representing a title, an author, and a publisher,
       and returns information regarding books.

    Args:
        title (str): Desired book Title
        author (str): Desired Author
        publisher (str): Desired Publisher

    Returns:
        str: All corresponding Books with the related inputs displaying neatly with appropriate headers and column spacing.
    """
    if title=="" and author=="" and publisher=="":
      mb.showerror(title="Error", message=f"Enter information for the Title, Author, and/or Publisher first.")
      return "No Results"
    bookList = ["Title", "Authors", "Publisher"] # Contains all strings needed for output.
    BookObjectsList = list() # Contains all Book objects needed.
    columnLengths = [5, 7, 9] # Desired Column Lengths for each column for proper display.
    flags = [1, 1, 1] # Boolean flags for checking if an input is blank.
    if title=="":
      flags[0] = 0 # Any flag set to 0 will not be used in the matching process.
    if author=="":
      flags[1] = 0
    if publisher=="":
      flags[2] = 0
    for bookInfo in self.__Books.values():
      bookIsMatch = True
      if flags[0]==1 and title!=bookInfo.getTitle(): # If there is a title inputted and it doesn't match, do not add book.
        bookIsMatch = False
      if flags[1]==1: # If there is an author inputted and it doesn't match, don't add book.
        authors_str = bookInfo.getAuthors()
        authors_str = authors_str.strip()
        authors = list(authors_str.split("\\"))
        authorFlag = False
        for person in authors: # Check if the inputted author's name is in the list of authors
          if author==person:
            authorFlag = True
        if not authorFlag:
          bookIsMatch = False
      if flags[2]==1 and publisher!=bookInfo.getPublishers(): # If there is a publisher inputted and it doesn't match, do not add book.
        bookIsMatch = False
      if bookIsMatch: # If everything matched, book is added.
        BookObjectsList.append(bookInfo) 
    for book in BookObjectsList:
      if len(book.getTitle())>columnLengths[0]:
        columnLengths[0] = len(book.getTitle())
      if len(book.getAuthors())>columnLengths[1]:
        columnLengths[1] = len(book.getAuthors())
      if len(book.getPublishers())>columnLengths[2]:
        columnLengths[2] = len(book.getPublishers())
      bookList.append(book.getTitle())
      bookList.append(book.getAuthors())
      bookList.append(book.getPublishers())
    output = str()
    count = 0
    for i in bookList:
      if count%3==0:
        output += f"\n{i}" + " "*(columnLengths[0]+4-len(i)) # Adds strings from the bookList using proper indenting
      elif count%3==2:
        output += f"{i}" # Adds strings 
      else:
        output += f"{i}" + " "*(columnLengths[count%3]+4-len(i)) # Adds strings from bookList using proper spacing
      count += 1
    return output
    
  def getRecommendations(self, media, title):
    """Takes in strings representing a type and a title, and returns a string
       containing recommendations regarding Movies, TV Shows, or Books.

    Args:
        media (str): Name of desired media type
        title (str): Name of desired title

    Returns:
        str: Recommended Movies, TV Shows, or Books with all of their information displayed line by line and with headers.
    """
    output = ""
    if media=="TV Show" or media=="Movie":
      for show in self.__Shows.items():
        if show[1].getTitle()==title:
          showID = show[0]
          break
      else:
        mb.showwarning(title="Warning", message=f"There are no recommendations for that title.")
        return "No results"
      relatedBooks = dict()
      relatedBooks = self.__Associations[showID] # Dictionary of related Book ids
      for bookKey in relatedBooks.keys():
        output += f"Title:\n{self.__Books[bookKey].getTitle()}\n"
        output += f"Authors:\n{self.__Books[bookKey].getAuthors()}\n"
        output += f"Average Rating:\n{self.__Books[bookKey].getAvgRating()}\n"
        output += f"ISBN:\n{self.__Books[bookKey].getIsbn()}\n"
        output += f"ISBN13:\n{self.__Books[bookKey].getIsbn13()}\n"
        output += f"Language Code:\n{self.__Books[bookKey].getLanguageCode()}\n"
        output += f"Pages:\n{self.__Books[bookKey].getNumPages()}\n"
        output += f"Rating Count:\n{self.__Books[bookKey].getNumRatings()}\n"
        output += f"Publication Date:\n{self.__Books[bookKey].getPubDate()}\n"
        output += f"Publisher:\n{self.__Books[bookKey].getPublishers()}\n"
        output += "****************************************************\n"
      return output
    elif media=="Book":
      for book in self.__Books.items():
        if book[1].getTitle()==title:
          bookID = book[0]
          break
      else:
        mb.showwarning(title="Warning", message=f"There are no recommendations for that title.")
        return "No results"
      relatedShows = dict()
      relatedShows = self.__Associations[bookID] # Dictionary of related Book ids
      for showKey in relatedShows.keys():
        output += f"Type:\n{self.__Shows[showKey].getType()}\n"
        output += f"Title:\n{self.__Shows[showKey].getTitle()}\n"
        output += f"Directors:\n{self.__Shows[showKey].getDirectors()}\n"
        output += f"Cast:\n{self.__Shows[showKey].getActors()}\n"
        output += f"Average Rating:\n{self.__Shows[showKey].getAvgRating()}\n"
        output += f"Country Code:\n{self.__Shows[showKey].getCountryCode()}\n"
        output += f"Date Added:\n{self.__Shows[showKey].getDateAdded()}\n"
        output += f"Year Released:\n{self.__Shows[showKey].getYear()}\n"
        output += f"Rating:\n{self.__Shows[showKey].getRating()}\n"
        output += f"Duration:\n{self.__Shows[showKey].getDuration()}\n"
        output += f"Genres:\n{self.__Shows[showKey].getGenres()}\n"
        output += f"Description:\n{self.__Shows[showKey].getDescription()}\n"
        output += "****************************************************\n"
      return output
    return "No results"
    
      