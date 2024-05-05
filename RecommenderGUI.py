import tkinter as tk
from tkinter import ttk
from Recommender import Recommender
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()

        self.main_window = tk.Tk()
        self.main_window.title("Recommender")
        self.main_window.geometry("1200x800")

        self.notebook = ttk.Notebook(self.main_window)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        self.tabMovies = ttk.Frame(self.notebook)
        self.notebook.add(self.tabMovies, text="Movies")

        self.moviesText = tk.Text(self.tabMovies, height=23, wrap=tk.WORD)
        self.moviesText.insert(tk.END, 'No movies found (yet)')
        self.moviesText.configure(state='disabled')
        self.moviesText.pack(fill=tk.X)

        self.movieStatsText = tk.Text(self.tabMovies, height=23, wrap=tk.WORD)
        self.movieStatsText.insert(tk.END, 'No movies found (yet)')
        self.movieStatsText.configure(state='disabled')
        self.movieStatsText.pack(fill=tk.X)

        self.tabTVShows = ttk.Frame(self.notebook)
        self.notebook.add(self.tabTVShows, text="TV Shows")

        self.showsText = tk.Text(self.tabTVShows, height=23, wrap=tk.WORD)
        self.showsText.insert(tk.END, 'No shows found (yet)')
        self.showsText.configure(state='disabled')
        self.showsText.pack(fill=tk.X)

        self.showStatsText = tk.Text(self.tabTVShows, height=23, wrap=tk.WORD)
        self.showStatsText.insert(tk.END, 'No shows found (yet)')
        self.showStatsText.configure(state='disabled')
        self.showStatsText.pack(fill=tk.X)

        self.tabBooks = ttk.Frame(self.notebook)
        self.notebook.add(self.tabBooks, text="Books")

        self.booksText = tk.Text(self.tabBooks, height=23, wrap=tk.WORD)
        self.booksText.insert(tk.END, 'No books found (yet)')
        self.booksText.configure(state='disabled')
        self.booksText.pack(fill=tk.X)

        self.bookStatsText = tk.Text(self.tabBooks, height=23, wrap=tk.WORD)
        self.bookStatsText.insert(tk.END, 'No books found (yet)')
        self.bookStatsText.configure(state='disabled')
        self.bookStatsText.pack(fill=tk.X)

        self.tabBonus = ttk.Frame(self.notebook)
        self.notebook.add(self.tabBonus, text="Ratings")

        self.buttonFrame = tk.Frame(self.main_window)
        self.buttonFrame.pack(side=tk.TOP)

        self.loadShowsButton = tk.Button(self.buttonFrame, text="Load Shows", command=self.load_shows)
        self.loadShowsButton.pack(side=tk.LEFT)

        self.loadBooksButton = tk.Button(self.buttonFrame, text="Load Books", command=self.load_books)
        self.loadBooksButton.pack(side=tk.LEFT)

        self.tabSearchMoviesShows = ttk.Frame(self.notebook)
        self.notebook.add(self.tabSearchMoviesShows, text="Search Movies/TV")

        self.tabSearchBooks = ttk.Frame(self.notebook)
        self.notebook.add(self.tabSearchBooks, text="Search Books")

        self.movieShowLabelType = tk.Label(self.tabSearchMoviesShows, text="Type: ")
        self.movieShowLabelType.grid(row=0, column=0, sticky='w')
        self.movieShowCbType = ttk.Combobox(self.tabSearchMoviesShows, values=['Movie', 'TV Show'], state='readonly')
        self.movieShowCbType.grid(row=0, column=1, sticky='ew')

        self.movieShowLabelTitle = tk.Label(self.tabSearchMoviesShows, text="Title: ")
        self.movieShowLabelTitle.grid(row=1, column=0, sticky='w')
        self.movieShowEntryTitle = ttk.Entry(self.tabSearchMoviesShows, width=80)
        self.movieShowEntryTitle.grid(row=1, column=1, columnspan=16, sticky='ew')

        self.movieShowLabelDirector = tk.Label(self.tabSearchMoviesShows, text="Director: ")
        self.movieShowLabelDirector.grid(row=2, column=0, sticky='w')
        self.movieShowEntryDirector = ttk.Entry(self.tabSearchMoviesShows, width=80)
        self.movieShowEntryDirector.grid(row=2, column=1, columnspan=16, sticky='ew')

        self.movieShowLabelActor = tk.Label(self.tabSearchMoviesShows, text="Actor: ")
        self.movieShowLabelActor.grid(row=3, column=0, sticky='w')
        self.movieShowEntryActor = ttk.Entry(self.tabSearchMoviesShows, width=80)
        self.movieShowEntryActor.grid(row=3, column=1, columnspan=16, sticky='ew')

        self.movieShowLabelGenre = tk.Label(self.tabSearchMoviesShows, text="Genre: ")
        self.movieShowLabelGenre.grid(row=4, column=0, sticky='w')
        self.movieShowEntryGenre = ttk.Entry(self.tabSearchMoviesShows, width=80)
        self.movieShowEntryGenre.grid(row=4, column=1, columnspan=16, sticky='ew')

        self.movieShowButtonSearch = tk.Button(self.tabSearchMoviesShows, text='Search', command=self.search_shows)
        self.movieShowButtonSearch.grid(row=5, column=0, sticky='w')

        self.movieShowText = tk.Text(self.tabSearchMoviesShows, width=160)
        self.movieShowText.insert(tk.END, 'Enter terms and click search to receive a recommendation!')
        self.movieShowText.configure(state='disabled')
        self.movieShowText.grid(row=6, column=0, columnspan=32)

        self.bookLabelTitle = tk.Label(self.tabSearchBooks, text="Title: ")
        self.bookLabelTitle.grid(row=0, column=0, sticky='w')
        self.bookEntryTitle = ttk.Entry(self.tabSearchBooks, width=80)
        self.bookEntryTitle.grid(row=0, column=1, columnspan=16, sticky='ew')

        self.bookLabelAuthor = tk.Label(self.tabSearchBooks, text="Author: ")
        self.bookLabelAuthor.grid(row=1, column=0, sticky='w')
        self.bookEntryAuthor = ttk.Entry(self.tabSearchBooks, width=80)
        self.bookEntryAuthor.grid(row=1, column=1, columnspan=16, sticky='ew')

        self.bookLabelPublisher = tk.Label(self.tabSearchBooks, text="Publisher: ")
        self.bookLabelPublisher.grid(row=2, column=0, sticky='w')
        self.bookEntryPublisher = ttk.Entry(self.tabSearchBooks, width=80)
        self.bookEntryPublisher.grid(row=2, column=1, columnspan=16, sticky='ew')

        self.bookButtonSearch = tk.Button(self.tabSearchBooks, text='Search', command=self.search_books)
        self.bookButtonSearch.grid(row=3, column=0, sticky='w')

        self.bookText = tk.Text(self.tabSearchBooks, width=160)
        self.bookText.insert(tk.END, 'Enter terms and click search to receive a recommendation!')
        self.bookText.configure(state='disabled')
        self.bookText.grid(row=4, column=0, columnspan=32)

    def load_shows(self):
        """Loads all of the data from a selected show file using an askopenfilename dialog.
        """
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        shows = self.recommender.loadShows()
        movieList = self.recommender.getMovieList()
        movieStats = self.recommender.getMovieStats()
        showList = self.recommender.getTVList()
        showStats = self.recommender.getTVStats()

        self.moviesText.configure(state='normal')
        self.moviesText.delete(1.0, tk.END)
        self.moviesText.insert(tk.END, movieList.strip())
        self.moviesText.configure(state='disabled')

        self.movieStatsText.configure(state='normal')
        self.movieStatsText.delete(1.0, tk.END)
        self.movieStatsText.insert(tk.END, "Ratings: \n")
        for rating, amount in movieStats[0].items():
            self.movieStatsText.insert(tk.END, f'{rating} {"%.2f" % round(amount*100, 2)}%\n')

        self.movieStatsText.insert(tk.END, f'\nAverage Movie Duration: {"%.2f" % round(movieStats[1], 2)} minutes\n')
        self.movieStatsText.insert(tk.END, f'\nMost Prolific Director: {movieStats[2]}\n')
        self.movieStatsText.insert(tk.END, f'\nMost Prolific Actor: {movieStats[3]}\n')
        self.movieStatsText.insert(tk.END, f'\nMost Frequent Genre: {movieStats[4]}\n')
        self.movieStatsText.configure(state='disabled')

        self.showsText.configure(state='normal')
        self.showsText.delete(1.0, tk.END)
        self.showsText.insert(tk.END, showList.strip())
        self.showsText.insert(tk.END, "\nRatings: \n")
        self.showsText.configure(state='disabled')

        self.showStatsText.configure(state='normal')
        self.showStatsText.delete(1.0, tk.END)
        self.showStatsText.insert(tk.END, 'Ratings:\n')

        for rating, amount in showStats[0].items():
            self.showStatsText.insert(tk.END, f'{rating} {"%.2f" % round(amount * 100, 2)}%\n')
        self.showStatsText.insert(tk.END, f'\nAverage Number of Seasons: {"%.2f" % round(showStats[1], 2)} seasons\n')
        self.showStatsText.insert(tk.END, f'\nMost Prolific Actor: {showStats[2]}\n')
        self.showStatsText.insert(tk.END, f'\nMost Frequent Genre: {showStats[3]}\n')
        self.showStatsText.configure(state='disabled')

        self.drawPieChart(axs[0], movieStats[0].keys(), movieStats[0].values(), "Movie Ratings")
        self.drawPieChart(axs[1], showStats[0].keys(), showStats[0].values(), "TV Show Ratings")
        canvas = FigureCanvasTkAgg(fig, master=self.tabBonus)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def load_books(self):

        books = self.recommender.loadBooks()
        bookList = self.recommender.getBookList()
        bookStats = self.recommender.getBookStats()

        self.booksText.configure(state='normal')
        self.booksText.delete(1.0, tk.END)
        self.booksText.insert(tk.END, bookList.strip())
        self.booksText.configure(state='disabled')

        self.bookStatsText.configure(state='normal')
        self.bookStatsText.delete(1.0, tk.END)

        self.bookStatsText.insert(tk.END, f'Average Page Count: {"%.2f" % round(bookStats[0], 2)} pages\n')
        self.bookStatsText.insert(tk.END, f'\nMost Prolific Author: {bookStats[1]}\n')
        self.bookStatsText.insert(tk.END, f'\nMost Prolific Publisher: {bookStats[2]}\n')
        self.bookStatsText.configure(state='disabled')

    def search_shows(self):
        show_type = self.movieShowCbType.get()
        title = self.movieShowEntryTitle.get()
        director = self.movieShowEntryDirector.get()
        actor = self.movieShowEntryActor.get()
        genre = self.movieShowEntryGenre.get()

        results = self.recommender.searchTVMovies(show_type, title, director, actor, genre)

        self.movieShowText.configure(state='normal')
        self.movieShowText.delete(1.0, tk.END)
        self.movieShowText.insert(tk.END, results.strip())
        self.movieShowText.configure(state='disabled')

    def search_books(self):
        title = self.bookEntryTitle.get()
        author = self.bookEntryAuthor.get()
        publisher = self.bookEntryPublisher.get()

        results = self.recommender.searchBooks(title, author, publisher)

        self.bookText.configure(state='normal')
        self.bookText.delete(1.0, tk.END)
        self.bookText.insert(tk.END, results.strip())
        self.bookText.configure(state='disabled')


    def drawPieChart(self, ax, labels, sizes, title):
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.set_title(title)
        ax.axis('equal')

def main():
    recommender_gui = RecommenderGUI()
    recommender_gui.main_window.mainloop()

if __name__ == "__main__":
    main()
