# Netflix Data Analysis Case Study – Content Strategy & Insight Generation

This project analyzes Netflix's content library to derive business insights on trends, genres, content types, and global presence. The goal is to help inform content strategy, including genre expansion, release focus, and multi-country production potential.

---

## 🔍 Project Breakdown

### 🧾 1. Data Understanding & Problem Definition
- Dataset: 8,807 titles across 12 features (title, director, cast, release_year, rating, etc.)
- Goal: Identify trends in Netflix content to guide strategic business decisions.

### 🛠️ 2. Data Cleaning & Preprocessing
- Missing values in `director`, `cast`, `country` filled with `"Unknown"`.
- Converted date fields to proper datetime format.
- Removed duplicates and ensured accurate data types.
- Memory optimized using categorical encoding.

### 📊 3. Univariate & Bivariate Visual Analysis
- `release_year`: Most content released post-2010; spike after 2015.
- `type`: Movies dominate, but TV shows are significant.
- `genre` (`listed_in`): Drama and International Movies top the list.
- Correlation: Strong negative correlation between release year and content age.

### 🧪 4. Feature Engineering
- `content_age` = current_year - release_year
- `num_genres` = count of genres per title
- `multi_country` = boolean flag for multi-country production

### 💡 5. Insights & Recommendations
- Content is predominantly fresh (under 10 years).
- Most titles are made in a single country.
- Drama, International, and Comedy are the most frequent genres.
- Few titles fall under Family or Documentary categories.

**Business Recommendations:**
- Expand multi-country production to increase global appeal.
- Invest more in underrepresented genres like Documentaries and Family Movies.
- Use content age and genre count as signals for personalized recommendations.

---

## 📁 Files Included

- `netflix-business-case-report.docx`  
- `netflix-business-case-report.pdf`  
- `netflix-cleaned-dataset.csv`  
- `netflix-analysis-script.py`

---

## 🛠 Tools Used

- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook
- Data Cleaning, Aggregation, Visualization
- Feature Engineering for business impact

---

> A strong foundation in using real-world data for content strategy, feature extraction, and actionable insights.
