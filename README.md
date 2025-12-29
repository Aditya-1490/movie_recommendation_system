🎬 Movie Recommendation System

A content-based movie recommendation system built using Natural Language Processing (NLP) techniques and Cosine Similarity, deployed as an interactive Streamlit web application.

🔗 Live Demo:
👉 https://movie-recommend-123.streamlit.app/

📌 Table of Contents

Project Overview

Problem Statement

Approach

Features

Tech Stack

Project Structure

Dataset

How It Works

Installation & Usage

Deployment

Results

Future Enhancements

Author

📖 Project Overview

This project recommends movies similar to a user-selected movie by analyzing movie metadata such as genres, overview, keywords, cast, and crew.
The system relies on content similarity, making it effective even when user interaction data is unavailable.

❓ Problem Statement

Users often struggle to discover movies aligned with their interests.
The goal of this project is to build a movie recommendation engine that suggests similar movies based on content rather than user ratings or behavior.

🧠 Approach

This is a content-based filtering system:

Combine important textual features into a single representation

Convert text data into numerical vectors

Compute similarity between movies

Recommend movies with the highest similarity score

🚀 Features

Recommend Top 5 similar movies

Content-based recommendation (no user history required)

Uses Cosine Similarity for distance measurement

Precomputed similarity matrix for fast responses

Interactive and simple Streamlit UI

Fully deployed and accessible online

🛠️ Tech Stack
Category	Tools
Programming Language	Python
Data Handling	Pandas, NumPy
NLP	Scikit-learn
Vectorization	CountVectorizer (Bag of Words)
Similarity Metric	Cosine Similarity
Web Framework	Streamlit
Deployment	Streamlit Cloud
📂 Project Structure
movie_recommendation_system/
│
├── app.py                   # Streamlit web application
├── Movie_recommender.ipynb  # Data analysis & model building
├── movies.pkl               # Processed movie dataframe
├── movies_dict.pkl          # Movie dictionary for UI
├── similarity.pkl           # Cosine similarity matrix
├── tmdb_5000_movies.csv     # Movies dataset
├── tmdb_5000_credits.csv    # Credits dataset
├── .gitignore
└── README.md

📊 Dataset

Source: TMDB (The Movie Database)

Size: ~5,000 movies

Key Features Used:

Movie title

Overview

Genres

Keywords

Cast

Crew

⚙️ How It Works

Data Preprocessing

Extract relevant columns

Clean and normalize text

Merge features into a single tags column

Vectorization

Apply Bag of Words (CountVectorizer)

Limit vocabulary size for efficiency

Similarity Calculation

Compute cosine similarity between all movies

Store similarity matrix using pickle

Recommendation

User selects a movie

System returns the most similar movies based on cosine similarity scores

▶️ Installation & Usage
Step 1: Clone the Repository
git clone https://github.com/<your-username>/movie-recommendation-system.git
cd movie-recommendation-system

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Application
streamlit run app.py

🌍 Deployment

The application is deployed using Streamlit Cloud.

🔗 Live Application:
https://movie-recommend-123.streamlit.app/

📈 Results

Accurate recommendations for movies with similar themes and genres

Fast inference due to precomputed similarity matrix

User-friendly interface suitable for non-technical users

🔮 Future Enhancements

Replace Bag of Words with TF-IDF

Add Word2Vec / Sentence Transformers

Fetch movie posters using TMDB API

Build a hybrid recommender (content + collaborative)

Add user personalization
