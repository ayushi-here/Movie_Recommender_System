# 🎬 Movie Recommender System

## 🌐 Visit the App

Check out the live application here: [Link](https://movie-recommender-system-a8pq.onrender.com)

## Overview

The Movie Recommender System is a web application designed to provide personalized movie recommendations based on user preferences. The system uses Natural Language Processing (NLP) techniques and cosine similarity to generate recommendations and is deployed on Render for public access.

## Features

- **🔍 Cosine Similarity**: Computes similarity between movies based on their features.
- **🧠 NLP Processing**: Utilizes text stemming to preprocess movie descriptions for better recommendations.
- **🌐 API Integration**: Fetches movie posters from the OMDB API and provides a RESTful API for recommendations.
- **💻 User Interface**: Built using Streamlit for an interactive and user-friendly experience.

## Project Structure

- `app.py`: Main application code that handles API requests, integrates with the recommendation system, and provides a Streamlit interface.
- `similarity.pkl`: Pickle file containing the precomputed similarity matrix.
- `movies_dict.pkl`: Pickle file containing movie metadata.
- `data/`: Directory containing the dataset and any other data files.
- `requirements.txt`: List of dependencies required for the project.