import joblib

print("Loading trained model...")

model_knn = joblib.load("knn_model.pkl")
movie_matrix = joblib.load("movie_matrix.pkl")
movies = joblib.load("movies_data.pkl")

def recommend_movies(movie_name):
    movie_name = movie_name.lower()

    matched = movies[movies['title'].str.lower().str.contains(movie_name)]

    if matched.empty:
        print("Movie not found!")
        return

    movie_id = matched.iloc[0]['movieId']

    if movie_id not in movie_matrix.index:
        print("Movie not found in matrix!")
        return

    index = movie_matrix.index.get_loc(movie_id)

    distances, indices = model_knn.kneighbors(
        movie_matrix.iloc[index, :].values.reshape(1, -1),
        n_neighbors=6
    )

    print("\nRecommended Movies:\n")

    for i in range(1, len(distances.flatten())):
        movie_index = movie_matrix.index[indices.flatten()[i]]
        title = movies[movies['movieId'] == movie_index]['title'].values[0]
        print(f"- {title}")


print("KNN Based Movie Recommendation System")

while True:
    user_input = input("\nEnter movie name (or exit): ")

    if user_input.lower() == "exit":
        break

    recommend_movies(user_input)
