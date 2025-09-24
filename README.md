# 🎬 Movie Recommender System

A content-based movie recommender system built with **Python, Scikit-learn, and Streamlit**.  
It suggests movies similar to a selected movie using cosine similarity.

---

## 🚀 Live Demo
👉 Try the app on Render: https://movie-recommender-system-c827.onrender.com/

---

## ⚙️ Features
- Recommends movies based on content similarity
- Uses **TF-IDF Vectorization** + **Cosine Similarity**
- Simple and interactive **Streamlit UI**
- Model files (`movies.pkl` and `similarity.pkl`) are stored in Google Drive and downloaded at runtime

---

## 🛠️ Installation (Run Locally)

1. Clone the repository:
   ```bash
   git clone https://github.com/luvsharma6342/movie-recommender-system.git
   cd movie-recommender-system
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
3. Install dependencies:
   ```
   pip install -r requirements.txt
4. Run the app:
   ```
   streamlit run app.py
## Model Files
Since model files are large, they are not stored in GitHub.
```
  movies.pkl
  similarity.pkl
```
These files are stored on Google Drive and automatically downloaded at runtime using the gdown package.

