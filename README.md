# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on user-selected titles. Built with Python and Streamlit, and containerized using Docker for easy deployment.

## 📌 Overview
This project leverages content-based filtering to recommend movies. By analyzing movie features, it computes similarities between movies and suggests titles that closely match the user's selection.

## 🚀 Features
- Content-Based Filtering: Recommends movies similar to the selected title using cosine similarity.
- Interactive UI: Built with Streamlit for a user-friendly interface.
- Dockerized Deployment: Easily deployable using Docker containers.
- TMDb API Integration: Fetches movie details and posters using The Movie Database API.

## 🛠️ Technologies Used
- Programming Language: Python
- Web Framework: Streamlit
- API Integration: TMDb API
- Containerization: Docker (Docker image: tkdutta/movierecommender)

## 📂 Project Structure
```env
movie_recommendation_system/
├── app/
│   ├── main.py
│   ├── utils.py
│   └── ...
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

## ⚙️ Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/tuhindutta/movie_recommendation_system.git
cd movie_recommendation_system
```
2. Set Up Environment Variables
Create a .env file in the root directory and add your TMDb API access token (API Read Access Token created in [https://www.themoviedb.org/](https://www.themoviedb.org/)):
```env
ACCESS_TOKEN=your_tmdb_api_access_token
```
3. Build and Run the Docker Container
```bash
docker run -d -p 8501:8501 --name movierecommender --env-file .env tkdutta/movierecommender:tag
```
The application will be accessible at `http://localhost:8501`

## 🧪 Usage
Upon accessing the application:
  1. Select a movie from the dropdown list.
  2. Click on the "Recommend" button.
  3. View a list of similar movies along with their posters and details.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
For more details and updates, visit the [GitHub Repository](https://github.com/tuhindutta/movie_recommendation_system).
