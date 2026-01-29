import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import joblib

print("Loading dataset...")

ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

print("Creating user-movie matrix...")

movie_user_matrix = ratings.pivot_table(
    index='movieId',
    columns='userId',
    values='rating'
).fillna(0)

matrix = csr_matrix(movie_user_matrix.values)

print("Training KNN model...")

model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(matrix)

print("Saving model...")

joblib.dump(model_knn, "knn_model.pkl")
joblib.dump(movie_user_matrix, "movie_matrix.pkl")
joblib.dump(movies, "movies_data.pkl")

print("Model training completed and saved successfully!")
