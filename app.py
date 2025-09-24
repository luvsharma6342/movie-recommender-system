import streamlit as st
import time
import pickle
import requests
import gdown


def fetch_poster(movie_id, max_retries=30):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=245d0cc8e922c356c6ad45f353e626e8&language=en-US'
    retry_count = 0

    while retry_count < max_retries:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Check if 'poster_path' exists
            if data.get('poster_path'):
                return "https://image.tmdb.org/t/p/w500" + data['poster_path']
            else:
                print(f"Poster not found for movie ID {movie_id}. Retrying...")

        except requests.exceptions.RequestException as e:
            print(f"Attempt {retry_count + 1} failed for movie ID {movie_id}: {e}")

        retry_count += 1
        time.sleep(2 ** retry_count)  # Exponential backoff: 2s, 4s, 8s, ...

    # Return fallback image after all retries fail
    return "https://via.placeholder.com/500x750?text=No+Image+Found"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

@st.cache_resource
def load_similarity():
    file_id = "1ksPSuJv2ZTXw7zEDGzvQA7ZzaRvVOFh8"
    url = f"https://drive.google.com/uc?id={file_id}"
    output = "similarity.pkl"

    # Download file (only once, thanks to caching)
    gdown.download(url, output, quiet=False)

    # Load pickle
    with open(output, "rb") as f:
        return pickle.load(f)

# Call the function to load your model/matrix
similarity = load_similarity()

movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be connected',
    movies['title'].values
)

if st.button('Recommend Movies'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])