import streamlit as st
import pickle
import pandas as pd

# App title
st.title("Movie Recommendation System")

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similar = pickle.load(open('similar.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Recommendation function
def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    # Get similarity scores for the movie
    distances = similar[movie_index]
    # Sort movies based on similarity scores and pick the top 5
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    # Fetch movie titles
    recommended_movies = [movies.iloc[i[0]]['title'] for i in movie_list]
    return recommended_movies

# Movie selection
selected_movie_name = st.selectbox(
    "Select Movie Name",
    movies['title'].values
)

# Recommendation button
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
