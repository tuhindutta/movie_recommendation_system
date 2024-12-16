# movie_recommendation_system

Docker image: https://hub.docker.com/repository/docker/tkdutta/movierecommender/general

To use perform the following steps:

1. Create a `.env` file containing the environment variable as following with an example:

`ACCESS_TOKEN={API Read Access Token created in https://www.themoviedb.org/}`


2. Execute the following command being in the same directory as the `.env` file to expose the application through 8501 port of localhost:

`docker run -d -p 8501:8501 --name movierecommender --env-file .env tkdutta/movierecommender:tag`
