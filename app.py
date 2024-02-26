import pickle 
import streamlit as st 
import pandas as pd 


def Recomanded(movie):
    movie_index = movies[movies['title']== movie].index[0]
    Distances = similarity[movie_index]
    movie_list =sorted(list(enumerate(Distances)), reverse = True ,key=lambda x:x[1]) [1:6]
    
    recomanded_movies = []
    for i in movie_list:
         # fetch poster 
         recomanded_movies.append(movies.iloc[i[0]].title)
    return recomanded_movies
    

movies_dict = pickle.load(open('movies_dict.pkl' ,'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl' ,'rb'))
st.title('Movie Recomanded system')

Selected_movie_name = st.selectbox('What kind of movies you want watch ? ' , movies['title'].values)

if st.button('Recomand'):
    recomandations =Recomanded(Selected_movie_name)
    for i in recomandations :
      st.write(i)