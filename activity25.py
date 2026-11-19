# Something about yourself
# 3 layer

yeah = "Look what your brother did to the door! Ain't he got no pride in his home?."
favorite_movie = "Wow, you know my favorite movie. That's good to know"
horror_type = "Yes that my favorite type of horror movie"
genre = "How did you know my favorite genre is horror?"

favorite_movie = {"Friday the 13th":"Guess", "My bloody valentine":"Incorrect", "Texan Chainsaw Massacre":yeah}
horror_type = {"Supernatural":"Right", "Monster":"Correct", "Psychological":"Absolutely", "Slasher":favorite_movie}
genre = {"Horror":horror_type, "Science Fiction":"fantasy_type", "Comedy":"comedy_type", "Romance":"romance_type"}
my_hobby = {"Watching":genre, "Eating":"favorite_food", "Playing":"card", "Sleeping":"Milk", "Reading":"SciFi"}

print(my_hobby["Watching"]([0][0][3][2]))