import webbrowser


class Movie():
    def __init__(self, Movie_Title, Movie_Story, Movie_Image, Movie_link):
        self.Movie_Title = Movie_Title
        self.Movie_Story = Movie_Story
        self.Movie_Image = Movie_Image
        self.Movie_link = Movie_link
    
    def display_trailer(self):
        webbrowser.open(self.Movie_link)
