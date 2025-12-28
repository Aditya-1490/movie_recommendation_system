# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
#
# # def fetch_posters(movie_id):
# #     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=310bbde2a1f39d268dabf2ff0b52d69a&language=en-US'.format(movie_id))
# #     data = response.json()
# #     return "https://image.tmdb.org/t/p/[size]/w500/" + data['poster_path']
#
# def fetch_posters(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}"
#     params = {
#         "api_key": "YOUR_API_KEY_HERE",
#         "language": "en-US"
#     }
#
#     try:
#         response = requests.get(url, params=params, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#
#         poster_path = data.get("poster_path")
#
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500" + poster_path
#         else:
#             return "https://via.placeholder.com/300x450?text=No+Poster"
#
#     except Exception as e:
#         return "https://via.placeholder.com/300x450?text=Error"
#
#
#
#
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]  # getting movie index
#     distances = similarity[index]
#     movies_list  = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetch posters
#         recommended_movies_posters.append(fetch_posters(movie_id))
#     return recommended_movies,recommended_movies_posters
#
# movies_dict =  pickle.load(open('movies_dict.pkl', 'rb'))
# movies= pd.DataFrame(movies_dict)
#
# similarity =  pickle.load(open('similarity.pkl', 'rb'))
#
# st.title('Movie Recommender System')
#
# selected_movie_name = st.selectbox(
# "How would you like to be contacted?",
# movies['title'].values
# )
#
# # if st.button('Recommend'):
# #     names,posters = recommend(selected_movie_name)
# #     col1,col2,col3,col4,col5 = st.columns(5)
# #     with col1:
# #         st.header(names[0])
# #         st.image(posters[0])
# #
# #     with col2:
# #         st.header(names[1])
# #         st.image(posters[1])
# #     with col3:
# #         st.header(names[2])
# #         st.image(posters[2])
# #     with col4:
# #         st.header(names[3])
# #         st.image(posters[3])
# #     with col5:
# #         st.header(names[4])
# #         st.image(posters[4])
#
# if st.button('Recommend'):
#     try:
#         names, posters = recommend(selected_movie_name)
#
#         col1, col2, col3, col4, col5 = st.columns(5)
#
#         with col1:
#             st.text(names[0])
#             st.image(posters[0])
#
#         with col2:
#             st.text(names[1])
#             st.image(posters[1])
#
#         with col3:
#             st.text(names[2])
#             st.image(posters[2])
#
#         with col4:
#             st.text(names[3])
#             st.image(posters[3])
#
#         with col5:
#             st.text(names[4])
#             st.image(posters[4])
#
#     except Exception as e:
#         st.error("Something went wrong while fetching recommendations.")
#         st.write(e)

import streamlit as st
import pickle
import pandas as pd
import requests


# -------------------------------
# TMDB API CONFIG
# -------------------------------
TMDB_API_KEY = "310bbde2a1f39d268dabf2ff0b52d69a"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
PLACEHOLDER_IMG = "https://via.placeholder.com/300x450?text=No+Poster"


# -------------------------------
# FETCH POSTER SAFELY
# -------------------------------
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return TMDB_IMAGE_BASE + poster_path
        else:
            return PLACEHOLDER_IMG

    except requests.exceptions.RequestException as e:
        print(f"TMDB error for movie_id {movie_id}: {e}")
        return PLACEHOLDER_IMG


# -------------------------------
# RECOMMEND FUNCTION
# -------------------------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# -------------------------------
# LOAD DATA
# -------------------------------
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# -------------------------------
# STREAMLIT UI
# -------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

# -------------------------------
# BUTTON ACTION
# -------------------------------
if st.button('Recommend'):
    try:
        names, posters = recommend(selected_movie_name)

        # Debug (remove later)
        # st.write(posters)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image(posters[0])
            st.caption(names[0])

        with col2:
            st.image(posters[1])
            st.caption(names[1])

        with col3:
            st.image(posters[2])
            st.caption(names[2])

        with col4:
            st.image(posters[3])
            st.caption(names[3])

        with col5:
            st.image(posters[4])
            st.caption(names[4])

    except Exception as e:
        st.error("Something went wrong while generating recommendations.")
        st.write(e)

