import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a642e71f2825c941a2bc4e8697ea59ed&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0] #masking
    movies_lt=sorted(list(enumerate(similarity_list[movie_index])),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    # print(movies_list)
    for i in movies_lt:
        movie_id=movies_list.iloc[i[0]].movie_id
        # fetch poster
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


# below code will give the new_df (dataframe)
movies_list=pickle.load(open('movies.pkl','rb'))
similarity_list=pickle.load(open('similarity.pkl','rb'))

# movies_list=movies_list['title'].values

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
'What\'s your favourite movie?',
movies_list['title'].values)

if st.button('Recommend'):
    recommended_names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        st.text(recommended_names[0])
        st.image(posters[0])
    with col2:
        st.text(recommended_names[1])
        st.image(posters[1])
    with col3:
        st.text(recommended_names[2])
        st.image(posters[2])
    with col4:
        st.text(recommended_names[3])
        st.image(posters[3])
    with col5:
        st.text(recommended_names[4])
        st.image(posters[4])

