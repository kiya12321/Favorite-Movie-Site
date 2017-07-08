import webbrowser


class Movie:
    """Attributes:
        movie_title: The movie's title.
        poster_image_url: The URL for the movie's poster art.
        trailer_youtube_url: The URL for the movie's Trailer
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
