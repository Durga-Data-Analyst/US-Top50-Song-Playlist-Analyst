# 🎵 United States Top 50 Playlist Performance and Song Popularity Trend Analysis

## 📌 Project Overview

The music streaming industry is highly dynamic, where playlist rankings directly impact artist visibility, listener engagement, and streaming revenue. This project analyzes historical United States Top 50 Playlist data to uncover patterns in song popularity, ranking stability, artist dominance, and content attributes.

The goal is to provide actionable insights that help record labels such as Atlantic Recording Corporation optimize promotion strategies, release timing, and marketing investments.

---

## 🎯 Business Problem

Despite having access to daily playlist rankings, stakeholders often struggle to answer key questions:

- Which songs remain relevant the longest?
- What differentiates stable chart performers from volatile ones?
- Which artists dominate playlists over time?
- How do song characteristics influence popularity and rankings?
- What role does explicit content play in streaming success?

This project transforms raw playlist data into meaningful business intelligence through exploratory data analysis and an interactive Streamlit dashboard.

---

## 📂 Dataset Description

| Column | Description |
|----------|-------------|
| date | Playlist snapshot date |
| position | Playlist rank (1-50) |
| song | Song title |
| artist | Artist name |
| popularity | Popularity score |
| duration_ms | Song duration in milliseconds |
| album_type | Single or Album |
| total_tracks | Number of tracks in album |
| is_explicit | Explicit content flag |
| album_cover_url | Album artwork URL |

---

## 🛠️ Tech Stack

### Programming & Analysis
- Python
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Dashboard
- Streamlit

### Version Control
- Git
- GitHub

---

## 📊 Key Performance Indicators (KPIs)

### Song Performance KPIs
- Days on Chart
- Average Rank
- Best Rank Achieved
- Rank Volatility Index
- Popularity Trend Score

### Artist KPIs
- Unique Songs per Artist
- Total Playlist Days
- Artist Dominance Index

### Content KPIs
- Explicit Content Share
- Album vs Single Performance
- Duration Impact Score

---

## ⚙️ Project Workflow

### 1. Data Cleaning & Validation

- Removed duplicate song-date entries
- Validated rank range (1–50)
- Standardized artist names
- Handled missing values
- Converted date formats
- Performed consistency checks

### 2. Feature Engineering

Created advanced metrics including:

- Days on Chart
- Average Rank
- Best Rank Achieved
- Rank Volatility Index
- Popularity Trend Score
- Duration in Minutes
- Artist Dominance Index

### 3. Exploratory Data Analysis

Performed comprehensive analysis across multiple dimensions:

#### Playlist Ranking Analysis
- Daily Rank Distribution
- Rank Movement Patterns
- Entry vs Exit Behavior
- Fast Risers Identification
- Slow Decliners Identification

#### Song-Level Performance Analysis
- Songs with Longest Playlist Presence
- Songs with Highest Average Popularity
- Peak Rank vs Longevity Comparison

#### Artist Performance Analysis
- Number of Unique Songs per Artist
- Total Days Artist Appears on Playlist
- Artist Dominance Over Time

#### Popularity Score Analytics
- Popularity vs Rank Correlation
- Popularity Distribution Across Top 10, Top 20 and Top 50
- Popularity Stability vs Chart Volatility

#### Content Attribute Analysis
- Explicit vs Non-Explicit Song Performance
- Single vs Album Track Comparison
- Song Duration Impact on Popularity and Rank
- Album Size Impact on Song Success

---

## 📈 Streamlit Dashboard Features

### Tab 1: KPI Overview
Displays:
- Total Songs
- Total Artists
- Average Popularity
- Average Rank
- Explicit Content Share

### Tab 2: Playlist Timeline Explorer
Displays:
- Song Ranking Trends
- Historical Rank Movement
- Playlist Timeline Analysis

### Tab 3: Song Performance Analysis
Displays:
- Longest Playlist Presence
- Fast Risers
- Slow Decliners
- Peak Rank vs Longevity Analysis

### Tab 4: Artist Dominance Leaderboard
Displays:
- Top Artists by Playlist Presence
- Number of Songs per Artist
- Artist Dominance Scores

### Tab 5: Popularity Analytics
Displays:
- Popularity vs Rank Scatter Plot
- Popularity Distribution
- Correlation Analysis

### Tab 6: Content Attribute Analysis
Displays:
- Explicit vs Non-Explicit Comparison
- Album vs Single Performance
- Duration Impact Analysis
- Album Size Impact Analysis

---

## 📊 Key Visualizations

### Playlist Analytics
- Daily Rank Distribution
- Ranking Trend Analysis
- Fast Risers and Slow Decliners

### Artist Analytics
- Artist Dominance Bar Chart
- Artist Presence Analysis

### Popularity Analytics
- Popularity vs Rank Scatter Plot
- Popularity Distribution Histogram
- Correlation Heatmap

### Content Analytics
- Explicit vs Non-Explicit Comparison
- Album Type Performance Analysis
- Duration Impact Regression Plot
- Album Size Impact Plot

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/us-top50-playlist-analysis.git
```

Navigate to the project folder:

```bash
cd us-top50-playlist-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 📌 Business Insights Generated

This project helps identify:

- Songs with long-term chart sustainability
- Artists dominating streaming playlists
- Relationship between popularity and ranking
- Impact of explicit content on performance
- Effect of song duration on listener engagement
- Influence of album structure on playlist success

---

## 🎯 Strategic Recommendations

### For Record Labels
- Prioritize artists with high chart persistence.
- Focus promotional efforts on songs showing positive rank momentum.
- Monitor rank volatility to identify declining tracks early.
- Leverage content attributes when planning releases.

### For Marketing Teams
- Optimize campaign timing around ranking momentum.
- Allocate budgets based on artist dominance metrics.
- Track playlist performance using analytical KPIs.

---

## 📈 Future Enhancements

- Real-Time Spotify API Integration
- Automated PDF Report Generation
- Artist-Level Forecasting
- Trend Anomaly Detection
- Interactive Plotly Visualizations
- Streamlit Cloud Deployment

---

## 👨‍💻 Author

### Durga Prasad Keshri

**Data Analyst | Business Analyst**

**Skills:** Python, SQL, Power BI, Tableau, Streamlit

📧 Email: keshridurgaprasad@gmail.com

🔗 LinkedIn:www.linkedin.com/in/durga-prasad-data-analyst

🔗 GitHub:https://github.com/Durga-Data-Analyst

---

### ⭐ If you found this project useful, consider giving it a star on GitHub.
