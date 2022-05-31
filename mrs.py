import streamlit as st
import pickle 
import requests

#df = pd.read_pickle('C://Users//Rezwan//Desktop//Projects//movies_rec.csv//movies.pkl')

movies_list = pickle.load( open('C://Users//Rezwan//Desktop//Projects//movies_rec//movies.pkl', 'rb'))

cs_score = pickle.load(open('C://Users//Rezwan//Desktop//Projects//movies_rec//cs_score.pkl', 'rb'))
movies = movies_list['title'].values

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=043b47e34820d9721f2530544085cae6&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']



def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = cs_score[movie_index]
    mo_list = sorted(list(enumerate(distances)), reverse= True, key = lambda x:x[1])[1:7]
    
    recommend_movies = []
    rec_mov_posters = []
    
    for i in mo_list:        
        recommend_movies.append(movies_list.iloc[i[0]].title)
        
        mo_id = movies_list.iloc[i[0]].id
        rec_mov_posters.append(fetch_poster(mo_id))
    return recommend_movies, rec_mov_posters

st.title('Movie Recommender System')

option = st.selectbox(
    'Chose Movie name:', movies)

if st.button('Recommend'):
    names, posters = recommend(option)
    
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)

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

    with col6:
        st.text(names[5])
        st.image(posters[5])

