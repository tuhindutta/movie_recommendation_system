import streamlit as st
from utility import *
# from credentials import *
import requests
import os

# token = apiReadAccessToken
token = os.getenv("ACCESS_TOKEN")


# Initialize session state keys if they don't already exist
if "search_dic" not in st.session_state:
    st.session_state.search_dic = None
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# App title
st.title("Movie Recommendation System")

# Input for the movie title
title = st.text_input("Movie title")

# Search button
if st.button("Search"):
    st.session_state.search_dic = search(title, token)

# Display dropdown only if search results are available
if st.session_state.search_dic:
    st.session_state.selected_movie = st.selectbox(
        "Movie title", list(st.session_state.search_dic.keys())
    )

    st.write(f"Selected Movie: {st.session_state.selected_movie}")

    if st.button("Recommend"):
        if st.session_state.selected_movie:
            movie_id = st.session_state.search_dic[st.session_state.selected_movie]
            st.session_state.recom = recommendations(movie_id, token)
            if st.session_state.recom:
                filteredImages = list(st.session_state.recom.values())
                st.image(filteredImages, width=100)
        else:
            st.write("Please select a movie from the dropdown.")