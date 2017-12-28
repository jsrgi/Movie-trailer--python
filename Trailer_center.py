import Movie
import fresh_tomatoes

pokemon_call_func=Movie.Movie("PokeMon","A story of Ase and his Pokemons,How to get a pokemon master award !!","https://www.billboard.com/files/styles/900_wide/public/media/pokemon-hero-ash-pikachu-2016-july-billboard-1548.jpg"
, "https://www.youtube.com/watch?v=pcUSRT7CFPs")
ShakalakkaBoomBoom_call_func=Movie.Movie("ShakalakkaBoomBoom","A story of boy and his Magic pencil !!","http://media2.intoday.in/indiatoday/images/stories/shaka-laka-647_051216123734.jpeg"
, "https://www.youtube.com/watch?v=J3UHc9F725Y")
Shinchan_call_func=Movie.Movie("Shinchan","A story of boy and his activities !!","https://shop.line-scdn.net/themeshop/v1/products/01/dd/f3/01ddf34d-b65b-438c-abd2-85088b5d375d/56/WEBSTORE/icon_198x278.png?__=20161019"
, "https://www.youtube.com/watch?v=u5nLECto_-U")
movie_list=[pokemon_call_func,ShakalakkaBoomBoom_call_func,Shinchan_call_func]
fresh_tomatoes.open_movies_page(movie_list)
