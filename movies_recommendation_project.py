import pandas as pd
import numpy as np
#read the file
df = pd.read_csv(r"C:\Users\LOQ\Desktop\Bollywood Movie List (1920-2024).csv")
df
#EDA

df.head()
df.tail()
df.describe
df.info()
df.columns
df.isnull().sum()
df.duplicated
#handling missing values and duplicates
df.drop_duplicates
df.dropna
df.isnull().sum()
df.duplicated


#I will use the movie name and Genre only so:
df_filtered = df[['Title', 'Genre']]

print(df_filtered)
df_filtered = df_filtered.reset_index(drop=True)
print(df_filtered)



df_filtered = df_filtered.dropna(subset=['Genre'])

print(df_filtered.isnull().sum())


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf= TfidfVectorizer(stop_words= 'english')

tfidf_matrix= tfidf.fit_transform(df_filtered['Genre'])
cosine_sim= cosine_similarity(tfidf_matrix,tfidf_matrix)
indices= pd.Series(df_filtered.index, index= df_filtered['Title'].str.lower())
print(indices['sholay'])

#building the recommendation model
def recommendation_system(movie_title, n_movies=6):
    title= movie_title.lower()
    if title not in indices:
        return "movie: {title} not available"
    
    index= indices[title]
    # Get similarity scores with all other movies
    similarity_scores = list(enumerate(cosine_sim[index]))
    
    # Sort movies by similarity (highest first)
    similarity_scores_sorted = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Take top n movies (skip the first one, which is the same movie)
    similarity_scores_sorted = similarity_scores_sorted[1:n_movies+1]
    movie_indices = [i[0] for i in similarity_scores_sorted]
    return df_filtered.iloc[movie_indices][['Title', 'Genre']]

#example usage
recommendation_system("sholay",4)    