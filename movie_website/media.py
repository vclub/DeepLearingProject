# coding=utf-8
import webbrowser

class Movie():
    """Movie Class

    [description]
    """

    def __init__(self, title, movie_storyline ,poster_image_url, trailer_url):
        """init movie 

        [description]
        
        Arguments:
            title {[string]} -- [movie name]
            movie_storyline {[string]} -- [movie storyline]
            poster_image_url {[string]} -- [movie poster image url]
            trailer_url {[string]} -- [movie trailer youtube url]
        """

        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        """open current movie trailer web page
        """
        webbrowser.open(self.trailer_url)
