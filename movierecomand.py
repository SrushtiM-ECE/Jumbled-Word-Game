# ------------------------------
# SIMPLE RECOMMENDATION SYSTEM
# ------------------------------

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------
# SAMPLE MOVIE DATA (You can change this)
# ---------------------------------------------

movies = pd.DataFrame({
    "movieId": [1, 2, 3, 4, 5],
    "title": ["Avatar", "Titanic", "Avengers", "Matrix", "Toy Story"]
})

ratings = pd.DataFrame({
    "userId": [1, 1, 1, 2, 2, 3, 3],
    "movieId": [1, 2, 3, 2, 4, 1, 5],
    "rating": [5, 4, 5, 5, 3, 4, 5]
})

# ---------------------------------------------
# BUILD USER-ITEM MATRIX
# ---------------------------------------------
user_item_matrix = ratings.pivot_table(
    index="userId",
    columns="movieId",
    values="rating"
).fillna(0)

# ---------------------------------------------
# ITEM-BASED COLLABORATIVE FILTERING
# ---------------------------------------------
item_similarity = cosine_similarity(user_item_matrix.T)

item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

def recommend_movies(user_id, top_k=3):
    if user_id not in user_item_matrix.index:
        return "User not found!"
    
    user_ratings = user_item_matrix.loc[user_id]
    watched = user_ratings[user_ratings > 0].index.tolist()

    scores = {}

    for movie in watched:
        similar_movies = item_similarity_df[movie].sort_values(ascending=False)
        for sim_movie, score in similar_movies.items():
            if sim_movie not in watched:
                scores[sim_movie] = scores.get(sim_movie, 0) + score

    # sort movies by similarity score
    recommended_ids = sorted(scores, key=scores.get, reverse=True)[:top_k]

    return movies[movies["movieId"].isin(recommended_ids)]

# ---------------------------------------------
#           TEST INPUT SECTION
# ---------------------------------------------
# Change this user_id to test
test_user_id = 1     # <-- ENTER USER ID HERE
top_k = 3            # <-- ENTER NUMBER OF RECOMMENDATIONS

print("Recommended movies for user:", test_user_id)
print(recommend_movies(test_user_id, top_k))
