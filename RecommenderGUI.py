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

        self.moviesText = tk.Text(self.tabMovies, wrap=tk.WORD)
        self.moviesText.pack()

        self.tabTVShows = ttk.Frame(self.notebook)
        self.notebook.add(self.tabTVShows, text="TV Shows")

        self.tvText = tk.Text(self.tabTVShows, wrap=tk.WORD)
        self.tvText.pack()

        self.tabBonus = ttk.Frame(self.notebook)
        self.notebook.add(self.tabBonus, text="Ratings")

        self.buttonFrame = tk.Frame(self.main_window)
        self.buttonFrame.pack(side=tk.TOP)

        self.loadShowsButton = tk.Button(self.buttonFrame, text="Load Shows", command=self.load_shows)
        self.loadShowsButton.pack(side=tk.LEFT)

    def load_shows(self):
        """Loads all of the data from a selected show file using an askopenfilename dialog.
        """
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        shows = self.recommender.loadShows()
        moviesList = self.recommender.getMovieList()
        moviesStats = self.recommender.getMovieStats()
        tvList = self.recommender.getTVList()
        tvStats = self.recommender.getTVStats()

        self.moviesText.delete(1.0, tk.END)
        self.moviesText.insert(tk.END, moviesList)
        self.moviesText.insert(tk.END, "\nRatings: \n")
        self.moviesText.insert(tk.END, moviesStats[0])

        self.tvText.delete(1.0, tk.END)
        self.tvText.insert(tk.END, tvList)
        self.tvText.insert(tk.END, "\nRatings: \n")
        self.tvText.insert(tk.END, tvStats[0])

        self.drawPieChart(axs[0], moviesStats[0].keys(), moviesStats[0].values(), "Movie Ratings")
        self.drawPieChart(axs[1], tvStats[0].keys(), tvStats[0].values(), "TV Show Ratings")
        canvas = FigureCanvasTkAgg(fig, master=self.tabBonus)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def drawPieChart(self, ax, labels, sizes, title):
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.set_title(title)
        ax.axis('equal')

def main():
    recommender_gui = RecommenderGUI()
    recommender_gui.main_window.mainloop()

if __name__ == "__main__":
    main()
