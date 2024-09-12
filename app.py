import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_title):
    api_key = 'c93dce45'
    url = f'http://www.omdbapi.com/?t={movie_title}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data.get('Poster', 'N/A') if data['Response'] == 'True' else 'N/A'

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_movies_posters.append(fetch_poster(movie_title))
    
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Page title and description
st.title('🎬 Movie Recommender System')
st.markdown("""
    **Find your next favorite movie!**  
    Select a movie and get personalized recommendations along with posters for each one.
""")

selected_movie_name = st.selectbox('Select a movie to get recommendations:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    st.subheader(f"Movies recommended based on *{selected_movie_name}*")
    
   
    cols = st.columns(5)  # Create 5 columns for the 5 recommendations
    
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_column_width=True)  # Set image to column width
            st.write(f"**{names[i]}**")  # Display movie title below the poster

