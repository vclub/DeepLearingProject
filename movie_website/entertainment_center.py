import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to li",
"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet",
"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.youtube.com/watch?v=9ceBgWV8io")

school_of_rock = media.Movie("School of Rock", "A marine on an alien planet",
"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
"https://www.youtube.com/watch?v=3PsUJFEBC74")

# print toy_story.storyline

MyFavorites = [toy_story, avatar, school_of_rock]

fresh_tomatoes.open_movies_page(MyFavorites)