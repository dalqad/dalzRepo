import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV
df_books = pd.read_csv(r"C:\Users\LOQ\Desktop\data.csv")

# Keep only title and authors (and we will add combined text)
df_books_filtered = df_books[['title', 'authors']].fillna('')

# Combine author + title for TF-IDF
df_books_filtered['author_title'] = df_books_filtered['title'] + " " + df_books_filtered['authors']

# TF-IDF
tfidf_ = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_.fit_transform(df_books_filtered['author_title'])

# Cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Search function
def search(author_name):
    # Find books by this author
    books = df_books_filtered[df_books_filtered['authors'].str.contains(author_name, case=False)]
    
    if books.empty:
        print("No books available for that author")
        return
    
    # Loop through books by this author
    for index, row in books.iterrows():
        print(row['title'] + " by " + row['authors'])
        
        # Similarity scores
        similarity_score = list(enumerate(cosine_sim[index]))
        similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        
        print("  Similar books:")
        for i, score in similarity_score[1:4]:  #to get the top 3
            print("   -", df_books_filtered.iloc[i]['title'], "by", df_books_filtered.iloc[i]['authors'])

# Run search/ enter any book author to search for
search("dali")
