# -*- coding: utf-8 -*-
import Media  # Imported from file
import fresh_tomatoes

# list of movies as defined.
lotr1 = Media.Movie("Lord of the Rings: The Fellowship of the Ring",
                    "https://goo.gl/tQZ7oI",
                    "https://www.youtube.com/watch?v=V75dMMIW2B4")
# Two hobbits make it a third of the way to Mordor.

lotr2 = Media.Movie("Lord of the Rings: The Two Towers",
                    "https://goo.gl/acVwVT",
                    "https://www.youtube.com/watch?v=LbfMDwc4azU")
# Two hobbits and their possessive pet make it two-thirds of the way to Mordor.

lotr3 = Media.Movie("Lord of the rings: The Return of the King",
                    "https://goo.gl/o3mPE8",
                    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")
# Two hobbits finally reach Mordor,
# where one suddenly forgets why he went there in the first place.

halloween = Media.Movie("Halloween",
                        "https://goo.gl/yHtFTF",
                        "https://www.youtube.com/watch?v=xHuOtLTQ_1I")
# A boy that just wants to spend halloween with new friends.

jaws = Media.Movie("Jaws",
                   "https://goo.gl/J8UJEi",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")
# A country with nuclear weapons can’t figure out a way to stop a shark.

lolita = Media.Movie("Lolita",
                     "https://goo.gl/tqo2TR",
                     "https://www.youtube.com/watch?v=gykHjlrWp2c")
# A man writes a 300+ page book to justify
# having sex with his 12 year old stepdaughter.

# script that creates web page
movies = (lotr1, lotr2, lotr3, halloween, jaws, lolita)
fresh_tomatoes.open_movies_page(movies)
