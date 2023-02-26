import spacy
nlp = spacy.load('en_core_web_md')


class Movie:
    """
    A class for creating movie objects containing a name and description
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


def movie_file_reader(file):
    """
    This function is intended to take a list of movies from a text file
    and store them in a list as objects
    :param file: .txt files containing movies where each movie is stored
    on a separate line in the format '{movie name} :{movie description}'
    :return: A list of Movie objects created from the text file.
    """
    movie_list = []
    with open(file) as movie_file:
        for line in movie_file:
            # As each movie name is separated from its description in
            # movies.txt by a ' :' we can split each line by this to get
            # the name and description separately.
            movie_details = line.rstrip().split(' :')
            new_movie = Movie(movie_details[0], movie_details[1])
            movie_list.append(new_movie)
    return movie_list


def next_movie(last_movie_desc, movie_list):
    """
    This is intended to recommend a movie from a list based on the description
    of the last movie watched by the user.
    :param last_movie_desc: The description of the last movie watched by the
    user
    :param movie_list: A list of Movie objects
    :return: The name of the movie from the movie_list with a description most
    similar to the description of the last movie watched.
    """
    desc_to_compare = nlp(last_movie_desc)
    similarity_dict = {}
    # First we compare the description of the last movie to the description
    # of all movies in the movie_list and create a dictionary with the movie
    # as the key and the similarity as the value
    for movie in movie_list:
        description_token = nlp(movie.description)
        movie_similarity = desc_to_compare.similarity(description_token)
        similarity_dict[movie] = movie_similarity

    # Now we find the key in the similarity dictionary with the highest
    # associated value and recommend this as the next movie to watch.
    recommended_movie = max(similarity_dict, key=similarity_dict.get)
    return recommended_movie.name


possible_recommendations = movie_file_reader("movies.txt")

hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the \
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to \
a planet where the Hulk can live in peace. Unfortunately, Hulk land on the \
planet Sakaar where he is sold into slavery and trained as a gladiator."""
last_movie_watched = Movie("Planet Hulk", hulk_description)

print(next_movie(last_movie_watched.description, possible_recommendations))
