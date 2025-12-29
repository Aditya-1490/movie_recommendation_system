## 🎬 Movie Recommendation System

A content-based movie recommendation system built using Natural Language Processing (NLP) techniques and Cosine Similarity, deployed as an interactive Streamlit web application.

🔗 Live Demo:
👉 https://movie-recommend-123.streamlit.app/


## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Approach](#approach)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Installation & Usage](#installation--usage)
- [Deployment](#deployment)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [Author](#author)



## 🚀 Features

- 🎬 Recommends **Top 5 similar movies**
- 🧠 Uses **content-based filtering**
- ⚡ Fast similarity search using **precomputed cosine similarity**
- 🌐 Interactive **Streamlit UI**
- 📊 Built using the **TMDB 5000 Movies Dataset**
- 🚀 Fully deployed and **production-ready**




## 🧠 Recommendation Approach

### 1️⃣ Data Processing
- Combined important textual features into a single **tags** column
- Cleaned and normalized text (lowercasing, removing spaces, etc.)

### 2️⃣ Vectorization
- Used **Bag of Words (CountVectorizer)** to convert text into numerical vectors

### 3️⃣ Similarity Calculation
- Computed **Cosine Similarity** between all movies
- Stored similarity matrix for fast lookup

### 4️⃣ Recommendation Logic
When a user selects a movie:
- Find its index
- Retrieve most similar movies using cosine similarity scores
- Return top recommendations





## 🛠️ Tech Stack
| Category      | Tools             |
| ------------- | ----------------- |
| Language      | Python            |
| Data Analysis | Pandas, NumPy     |
| NLP           | Scikit-learn      |
| ML Technique  | Cosine Similarity |
| Web App       | Streamlit         |
| Dataset       | TMDB 5000 Movies  |
| Deployment    | Streamlit Cloud   |





## 📂 Project Structure

```text
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
```







## 🧪 Dataset Information

**Source:** TMDB (The Movie Database)  
**Size:** ~5000 movies  

**Features Used:**
- Title
- Overview
- Genres
- Keywords
- Cast
- Crew



## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the App
```bash
streamlit run app.py
```

## 📈 Example Output

**Input:**  
Inception

**Recommendations:**
- Interstellar
- The Prestige
- Shutter Island
- The Dark Knight
- Memento

---

## 🌍 Deployment

The application is deployed using **Streamlit Cloud**.

🔗 **Live Demo:**  
https://movie-recommend-123.streamlit.app/

---

## 📸 Application Screenshot

![Movie Recommender System – Live Demo](screenshots/app_ui.png)









