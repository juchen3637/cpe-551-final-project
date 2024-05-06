# Author: Daniel Baton
# Date: 5/5/2024
# Description: GUI for the Recommender using the tkinter and matplot libraries

import tkinter as tk
from tkinter import ttk
from Recommender import Recommender
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RecommenderGUI:
    def __init__(self):
        # Create the recommender instance
        self.__recommender = Recommender()

        # Create the main window for the application
        self.__main_window = tk.Tk()
        self.__main_window.title("Recommender")
        self.__main_window.geometry("1200x800")

        # --- Buttons Frame ---
        self.__buttonFrame = tk.Frame(self.__main_window)
        self.__buttonFrame.pack(side=tk.BOTTOM)

        # Button to load shows
        self.__loadShowsButton = tk.Button(self.__buttonFrame, text="Load Shows", command=self.load_shows)
        self.__loadShowsButton.pack(side=tk.LEFT, padx=50)

        # Button to load books
        self.__loadBooksButton = tk.Button(self.__buttonFrame, text="Load Books", command=self.load_books)
        self.__loadBooksButton.pack(side=tk.LEFT, padx=50)

        # Button to load recommendations
        self.__loadRecsButton = tk.Button(self.__buttonFrame, text="Load Recommendations",
                                          command=self.load_associations)
        self.__loadRecsButton.pack(side=tk.LEFT, padx=50)

        # Button to display information
        self.__showInfoButton = tk.Button(self.__buttonFrame, text="Information", command=self.creditInfoBox)
        self.__showInfoButton.pack(side=tk.LEFT, padx=50)

        # Button to quit the application
        self.__quitButton = tk.Button(self.__buttonFrame, text="Quit", command=self.__main_window.destroy)
        self.__quitButton.pack(side=tk.LEFT, padx=50)

        # --- Notebook ---
        self.__notebook = ttk.Notebook(self.__main_window)
        self.__notebook.pack(side=tk.TOP)

        # --- Movies Tab ---
        self.__tabMovies = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tabMovies, text="Movies")

        # Text widget to display movies
        self.__moviesText = tk.Text(self.__tabMovies, height=23, wrap=tk.WORD)
        self.__moviesText.insert(tk.END, 'No movies found (yet)')
        self.__moviesText.configure(state='disabled')
        self.__moviesText.pack(fill=tk.BOTH)

        # Text widget to display movie stats
        self.__movieStatsText = tk.Text(self.__tabMovies, wrap=tk.WORD, height=23)
        self.__movieStatsText.insert(tk.END, 'No movies found (yet)')
        self.__movieStatsText.configure(state='disabled')
        self.__movieStatsText.pack(fill=tk.BOTH)

        # --- TV Shows Tab ---
        self.__tabTVShows = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tabTVShows, text="TV Shows")

        # Text widget to display TV shows
        self.__showsText = tk.Text(self.__tabTVShows, height=23, wrap=tk.WORD)
        self.__showsText.insert(tk.END, 'No shows found (yet)')
        self.__showsText.configure(state='disabled')
        self.__showsText.pack(fill=tk.BOTH)

        # Text widget to display TV show stats
        self.__showStatsText = tk.Text(self.__tabTVShows, height=23, wrap=tk.WORD)
        self.__showStatsText.insert(tk.END, 'No shows found (yet)')
        self.__showStatsText.configure(state='disabled')
        self.__showStatsText.pack(fill=tk.BOTH)

        # --- Books Tab ---
        self.__tabBooks = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tabBooks, text="Books")

        # Text widget to display books
        self.__booksText = tk.Text(self.__tabBooks, height=23, wrap=tk.WORD)
        self.__booksText.insert(tk.END, 'No books found (yet)')
        self.__booksText.configure(state='disabled')
        self.__booksText.pack(fill=tk.X)

        # Text widget to display book stats
        self.__bookStatsText = tk.Text(self.__tabBooks, height=23, wrap=tk.WORD)
        self.__bookStatsText.insert(tk.END, 'No books found (yet)')
        self.__bookStatsText.configure(state='disabled')
        self.__bookStatsText.pack(fill=tk.X)

        # --- Ratings Tab ---
        self.__tabBonus = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tabBonus, text="Ratings")

        # --- Search Movies/TV Tab ---
        self.__tabSearchMoviesShows = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tabSearchMoviesShows, text="Search Movies/TV")

        # Label + Combobox for Type
        self.__movieShowLabelType = tk.Label(self.__tabSearchMoviesShows, text="Type: ")
        self.__movieShowLabelType.grid(row=0, column=0, sticky='w')
        self.__movieShowCbType = ttk.Combobox(self.__tabSearchMoviesShows, values=['Movie', 'TV Show'], state='readonly')
        self.__movieShowCbType.grid(row=0, column=1, sticky='ew')

        # Label + Entry for Title
        self.__movieShowLabelTitle = tk.Label(self.__tabSearchMoviesShows, text="Title: ")
        self.__movieShowLabelTitle.grid(row=1, column=0, sticky='w')
        self.__movieShowEntryTitle = ttk.Entry(self.__tabSearchMoviesShows, width=80)
        self.__movieShowEntryTitle.grid(row=1, column=1, columnspan=16, sticky='ew')

        # Label + Entry for Director
        self.__movieShowLabelDirector = tk.Label(self.__tabSearchMoviesShows, text="Director: ")
        self.__movieShowLabelDirector.grid(row=2, column=0, sticky='w')
        self.__movieShowEntryDirector = ttk.Entry(self.__tabSearchMoviesShows, width=80)
        self.__movieShowEntryDirector.grid(row=2, column=1, columnspan=16, sticky='ew')

        # Label + Entry for Actor
        self.__movieShowLabelActor = tk.Label(self.__tabSearchMoviesShows, text="Actor: ")
        self.__movieShowLabelActor.grid(row=3, column=0, sticky='w')
        self.__movieShowEntryActor = ttk.Entry(self.__tabSearchMoviesShows, width=80)
        self.__movieShowEntryActor.grid(row=3, column=1, columnspan=16, sticky='ew')

        # Label + Entry for Genre
        self.__movieShowLabelGenre = tk.Label(self.__tabSearchMoviesShows, text="Genre: ")
        self.__movieShowLabelGenre.grid(row=4, column=0, sticky='w')
        self.__movieShowEntryGenre = ttk.Entry(self.__tabSearchMoviesShows, width=80)
        self.__movieShowEntryGenre.grid(row=4, column=1, columnspan=16, sticky='ew')

        # Button to perform the search
        self.__movieShowButtonSearch = tk.Button(self.__tabSearchMoviesShows, text='Search', command=self.search_shows)
        self.__movieShowButtonSearch.grid(row=5, column=0, sticky='w')

        # Text widget to display search results
        self.__movieShowText = tk.Text(self.__tabSearchMoviesShows, width=160, height=38)
        self.__movieShowText.insert(tk.END, 'Enter terms and click search to receive a recommendation!')
        self.__movieShowText.configure(state='disabled')
        self.__movieShowText.grid(row=6, column=0, columnspan=32)

        # --- Search Books Tab ---
        self.__tabSearchBooks = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tabSearchBooks, text="Search Books")

        # Label + Entry for Title
        self.__bookLabelTitle = tk.Label(self.__tabSearchBooks, text="Title: ")
        self.__bookLabelTitle.grid(row=0, column=0, sticky='w')
        self.__bookEntryTitle = ttk.Entry(self.__tabSearchBooks, width=80)
        self.__bookEntryTitle.grid(row=0, column=1, columnspan=16, sticky='ew')

        # Label + Entry for Author
        self.__bookLabelAuthor = tk.Label(self.__tabSearchBooks, text="Author: ")
        self.__bookLabelAuthor.grid(row=1, column=0, sticky='w')
        self.__bookEntryAuthor = ttk.Entry(self.__tabSearchBooks, width=80)
        self.__bookEntryAuthor.grid(row=1, column=1, columnspan=16, sticky='ew')

        # Label + Entry for Publisher
        self.__bookLabelPublisher = tk.Label(self.__tabSearchBooks, text="Publisher: ")
        self.__bookLabelPublisher.grid(row=2, column=0, sticky='w')
        self.__bookEntryPublisher = ttk.Entry(self.__tabSearchBooks, width=80)
        self.__bookEntryPublisher.grid(row=2, column=1, columnspan=16, sticky='ew')

        # Button to perform search
        self.__bookButtonSearch = tk.Button(self.__tabSearchBooks, text='Search', command=self.search_books)
        self.__bookButtonSearch.grid(row=3, column=0, sticky='w')

        # Text widget to display search results
        self.__bookText = tk.Text(self.__tabSearchBooks, width=160, height=40)
        self.__bookText.insert(tk.END, 'Enter terms and click search to receive a recommendation!')
        self.__bookText.configure(state='disabled')
        self.__bookText.grid(row=4, column=0, columnspan=32)

        # --- Recommendations Tab ---
        self.__tabRecommend = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tabRecommend, text="Recommendations")

        # Label + Combobox for Type
        self.__recommendLabelType = tk.Label(self.__tabRecommend, text="Type: ")
        self.__recommendLabelType.grid(row=0, column=0, sticky='w')
        self.__recommendCbType = ttk.Combobox(self.__tabRecommend, values=['Movie', 'TV Show', 'Book'], state='readonly')
        self.__recommendCbType.grid(row=0, column=1, sticky='ew')

        # Label + Entry for Title
        self.__recommendLabelTitle = tk.Label(self.__tabRecommend, text="Title: ")
        self.__recommendLabelTitle.grid(row=1, column=0, sticky='w')
        self.__recommendEntryTitle = ttk.Entry(self.__tabRecommend, width=80)
        self.__recommendEntryTitle.grid(row=1, column=1, columnspan=16, sticky='ew')

        # Button to perform recommendation
        self.__recommendButtonGet = tk.Button(self.__tabRecommend, text="Get Recommendation",
                                            command=self.get_recommendations)
        self.__recommendButtonGet.grid(row=2, column=0, sticky='w')

        # Text widget to display recommendation results
        self.__recommendText = tk.Text(self.__tabRecommend, width=160, height=41)
        self.__recommendText.insert(tk.END, 'Enter a type and title and click the button to receive a recommendation!')
        self.__recommendText.configure(state='disabled')
        self.__recommendText.grid(row=3, column=0, columnspan=32)

    def load_shows(self):
        """
        Loads all of the data from a selected show file using an askopenfilename dialog.
        """
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        for widget in self.__tabBonus.winfo_children():
          widget.destroy()

        # Load all necessary data from the recommender for shows and movies
        self.__recommender.loadShows()
        movieList = self.__recommender.getMovieList()
        movieStats = self.__recommender.getMovieStats()
        showList = self.__recommender.getTVList()
        showStats = self.__recommender.getTVStats()

        # Edit the text of the upper widget to display the list of movies
        self.__moviesText.configure(state='normal')
        self.__moviesText.delete(1.0, tk.END)
        self.__moviesText.insert(tk.END, movieList.strip())
        self.__moviesText.configure(state='disabled')

        # Edit the text of the lower widget to display the movie stats
        self.__movieStatsText.configure(state='normal')
        self.__movieStatsText.delete(1.0, tk.END)
        self.__movieStatsText.insert(tk.END, "Ratings: \n")
        for rating, amount in movieStats[0].items():
            self.__movieStatsText.insert(tk.END, f'{rating} {"%.2f" % round(amount*100, 2)}%\n')

        # ... even more movie stats ...
        self.__movieStatsText.insert(tk.END, f'\nAverage Movie Duration: {"%.2f" % round(movieStats[1], 2)} minutes\n')
        self.__movieStatsText.insert(tk.END, f'\nMost Prolific Director: {movieStats[2]}\n')
        self.__movieStatsText.insert(tk.END, f'\nMost Prolific Actor: {movieStats[3]}\n')
        self.__movieStatsText.insert(tk.END, f'\nMost Frequent Genre: {movieStats[4]}\n')
        self.__movieStatsText.configure(state='disabled')

        # Edit the text of the upper widget to display the list of TV shows
        self.__showsText.configure(state='normal')
        self.__showsText.delete(1.0, tk.END)
        self.__showsText.insert(tk.END, showList.strip())
        self.__showsText.insert(tk.END, "\nRatings: \n")
        self.__showsText.configure(state='disabled')

        # Edit the text of the lower widget to display the TV show stats
        self.__showStatsText.configure(state='normal')
        self.__showStatsText.delete(1.0, tk.END)
        self.__showStatsText.insert(tk.END, 'Ratings:\n')
        for rating, amount in showStats[0].items():
            self.__showStatsText.insert(tk.END, f'{rating} {"%.2f" % round(amount * 100, 2)}%\n')

        # ... even more tv show stats ...
        self.__showStatsText.insert(tk.END, f'\nAverage Number of Seasons: {"%.2f" % round(showStats[1], 2)} seasons\n')
        self.__showStatsText.insert(tk.END, f'\nMost Prolific Actor: {showStats[2]}\n')
        self.__showStatsText.insert(tk.END, f'\nMost Frequent Genre: {showStats[3]}\n')
        self.__showStatsText.configure(state='disabled')

        # Populate the pie chart with the movie and TV show rating data
        self.drawPieChart(axs[0], movieStats[0].keys(), movieStats[0].values(), "Movie Ratings")
        self.drawPieChart(axs[1], showStats[0].keys(), showStats[0].values(), "TV Show Ratings")

        # Draw the pie chart
        canvas = FigureCanvasTkAgg(fig, master=self.__tabBonus)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def load_books(self):
        """
        Loads all of the data from a selected book file using an askopenfilename dialog.
        """
        # Load all necessary information from the recommender for books
        self.__recommender.loadBooks()
        bookList = self.__recommender.getBookList()
        bookStats = self.__recommender.getBookStats()

        # Edit the text of the upper widget to display the list of books
        self.__booksText.configure(state='normal')
        self.__booksText.delete(1.0, tk.END)
        self.__booksText.insert(tk.END, bookList.strip())
        self.__booksText.configure(state='disabled')

        # Edit the text of the lower widget to display the book stats
        self.__bookStatsText.configure(state='normal')
        self.__bookStatsText.delete(1.0, tk.END)
        self.__bookStatsText.insert(tk.END, f'Average Page Count: {"%.2f" % round(bookStats[0], 2)} pages\n')
        self.__bookStatsText.insert(tk.END, f'\nMost Prolific Author: {bookStats[1]}\n')
        self.__bookStatsText.insert(tk.END, f'\nMost Prolific Publisher: {bookStats[2]}\n')
        self.__bookStatsText.configure(state='disabled')

    def load_associations(self):
        """
        Loads all of the data from a selected book file using an askopenfilename dialog.
        """
        self.__recommender.loadAssociations()  # Call the load associations function from the Recommender file

    def search_shows(self):
        """
        Performs a search for movies or TV shows using the corresponding recommender method.
        """
        # Get all necessary fields from the movie/TV show search widgets
        show_type = self.__movieShowCbType.get()
        title = self.__movieShowEntryTitle.get()
        director = self.__movieShowEntryDirector.get()
        actor = self.__movieShowEntryActor.get()
        genre = self.__movieShowEntryGenre.get()

        # Call the search TV shows/movies function from the Recommender file
        results = self.__recommender.searchTVMovies(show_type, title, director, actor, genre)

        # Edit the text of the widget to display the search results
        self.__movieShowText.configure(state='normal')
        self.__movieShowText.delete(1.0, tk.END)
        self.__movieShowText.insert(tk.END, results.strip())
        self.__movieShowText.configure(state='disabled')

    def search_books(self):
        """
        Performs a search for books using the corresponding recommender method.
        """
        # Get all necessary fields from the book search widgets
        title = self.__bookEntryTitle.get()
        author = self.__bookEntryAuthor.get()
        publisher = self.__bookEntryPublisher.get()

        # Call the search books function from the Recommender file
        results = self.__recommender.searchBooks(title, author, publisher)

        # Edit the text of the widget to display the search results
        self.__bookText.configure(state='normal')
        self.__bookText.delete(1.0, tk.END)
        self.__bookText.insert(tk.END, results.strip())
        self.__bookText.configure(state='disabled')

    def get_recommendations(self):
        """
        Gives the user recommendations of movies, tv shows, or books, using the corresponding recommender method.
        """
        # Get all necessary fields from the recommender widgets
        media_type = self.__recommendCbType.get()
        title = self.__recommendEntryTitle.get()
        results = self.__recommender.getRecommendations(media_type, title)

        # Edit the text of the widget to display the recommendation results
        self.__recommendText.configure(state='normal')
        self.__recommendText.delete(1.0, tk.END)
        self.__recommendText.insert(tk.END, results.strip())
        self.__recommendText.configure(state='disabled')

    def creditInfoBox(self):
        """
        Displays info about the creators
        """
        infoText = "Group Members: Daniel Baton, Justin Chen, Joseph Stefanoni\n" \
                   "Completed on 5/5/5024"
        tk.messagebox.showinfo("Information", infoText)

    def drawPieChart(self, ax, labels, sizes, title):
        """
        Displays a pie chart with information about different media. *Extra credit*
        """
        fig = plt.gcf()
        fig.set_size_inches(12, 6)

        explode = [0.3 if size < max(sizes) / 5 else 0 for size in sizes]
        ax.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90, explode=explode, pctdistance=0.9)
        ax.set_title(title)
        ax.axis('equal')

        plt.tight_layout()

    def main_loop(self):
        self.__main_window.mainloop()


def main():
    recommender_gui = RecommenderGUI()
    recommender_gui.main_loop()


if __name__ == "__main__":
    main()
