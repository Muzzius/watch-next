# watch-next
 Created for Hyperiondev Software Engineer Bootcamp L3T12

## Purpose
This project was created as part of a task for the Hyperiondev Software Engineer bootcamp. 
The purpose of this script was to create a function to compare the similarity of the description of the last movie a user to a list of movie descriptions
stored in a movies.txt file and output the name of the most similar movie as a recommendation to watch next.

## Requriements
1. Python 3 (https://www.python.org/downloads/)
2. pip (https://pip.pypa.io/en/stable/installation/)

## Installation
1. Clone the repository to a directory on your computer.
2. In command line navigate to the directory and run 'pip install -r requirements.txt'

## Usage
Currently the script is only hard coded to compare the similarity of the description of Planet Hulk to a list of movies in movies.txt.
To edit the last movie that is being compared to the movies in movie list you currently have manually edit the inputs for the next_movie function inside the print command on line 72.
To change the list of movies this is being compared to you can either edit movies.txt or create your own text file. In the text file each movie has to be on a new line
in the format [movie name] :[movie description] or the script will not work.
If you want to make your own text file you will need to replace "movies.txt" in the movie_file_reader function call on line 63.

You can run the script either through an IDE of your choice or in command prompt using the command 'python watch_next.py' in the root directory of the project. 
I have also provider a Dockerfile so you can creat an image of the project and run it in a container using Docker.
The output should look like this:

![watchnext](https://user-images.githubusercontent.com/15369629/221997695-7348ff92-2b35-4f23-b9cb-31186a3cc9cc.PNG)

## Running in a container
To run this project in a container you will either need to install Docker Decktop (https://www.docker.com/) or creat an account on Docker and use Docker Playground (https://labs.play-with-docker.com/)

### To run with Docker Desktop
1. Using command line in the root directory for the project (where the Dockerfile is found) run 
   'docker build -t [Enter a tag for the image] ./'
2. Once this has finished you can now run the script using
   'docker run [the tag you chose]'

### To run in docker playground
1. Follow step 1 from the Docker Desktop instructions to build the image.
2. In command line enter 'docker login' and enter your login details for docker hub.
3. On docker hub you will need to create a repository and then retag the local image to match your repository's name.
   to do this in command line run
   'docker tag [local tag for the image] [user]/[repo]'
   where user is your Docker hub username and repo is the repositories name.
4. Now upload the image by entering
   'docker push [user]/[repo]'
5. Now you can login to Docker playground with your Docker account and start a session and begin a new instance/
6. In the instance enter
   'docker run [user]/[repo]'

This should return a result similar to the example above.

## Credits
- Murray Bosworth
- https://www.hyperiondev.com/ for their course resources
