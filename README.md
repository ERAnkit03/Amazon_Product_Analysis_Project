# 🛒 Amazon Product Analysis Dashboard

## 📌 Project Overview

This project is a complete Exploratory Data Analysis (EDA) project built using Python and popular data analysis libraries. The goal of this project is to analyze Amazon product data to discover meaningful business insights related to:

* Product pricing
* Discounts
* Ratings
* Product categories
* Customer reviews
* Product popularity

The project demonstrates real-world data cleaning, preprocessing, analysis, and visualization techniques used in Data Analytics and Data Science.

---

# 🚀 Project Objectives

The main objectives of this project are:

✅ Clean and preprocess raw Amazon product data
✅ Perform exploratory data analysis (EDA)
✅ Analyze pricing and discount patterns
✅ Identify top-rated and most-reviewed products
✅ Analyze category-wise product distribution
✅ Create visualizations for better business understanding
✅ Generate actionable business insights

---

# 🧰 Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Programming Language      |
| Pandas           | Data Cleaning & Analysis  |
| NumPy            | Numerical Operations      |
| Matplotlib       | Data Visualization        |
| Seaborn          | Statistical Visualization |
| Jupyter Notebook | Interactive Analysis      |
| VS Code          | Development Environment   |

---

# 📂 Project Structure

```bash
Amazon_Product_Analysis/
│
├── data/
│   └── amazon.csv
│
├── notebooks/
│   └── amazon_analysis.ipynb
│
├── images/
│   ├── category_chart.png
│   ├── heatmap.png
│   ├── price_distribution.png
│   └── ratings_chart.png
│
├── reports/
│   └── cleaned_amazon_data.csv
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Information

The dataset contains Amazon product information including:

| Column Name         | Description              |
| ------------------- | ------------------------ |
| product_name        | Name of product          |
| category            | Product category         |
| discounted_price    | Discounted product price |
| actual_price        | Original product price   |
| discount_percentage | Discount offered         |
| rating              | Product rating           |
| rating_count        | Number of ratings        |
| about_product       | Product description      |
| user_review         | Customer reviews         |

---

# 🧹 Data Cleaning Process

Real-world datasets are often messy and require preprocessing.

The following cleaning operations were performed:

## ✔ Removed Currency Symbols

Example:

```python
₹1,299 → 1299
```

---

## ✔ Converted Datatypes

Converted:

* Prices → float
* Ratings → float
* Rating count → numeric

---

## ✔ Removed Missing Values

```python
df.dropna(inplace=True)
```

---

## ✔ Removed Commas & Percentage Symbols

Example:

```python
45% → 45
```

---

# 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

---

# 1️⃣ Product Category Analysis

Analyzed:

* Most common categories
* Product distribution by category

### Visualization:

* Bar charts
* Count plots

### Insight:

Electronics products dominate the dataset.

---

# 2️⃣ Price Analysis

Analyzed:

* Actual prices
* Discounted prices
* Price distributions

### Visualization:

* Histograms
* Boxplots

### Insight:

Most products are priced below ₹1000.

---

# 3️⃣ Discount Analysis

Analyzed:

* Highest discounted products
* Average discount percentage
* Discount trends

### Visualization:

* Bar charts
* Distribution plots

### Insight:

Large discounts do not always guarantee high ratings.

---

# 4️⃣ Rating Analysis

Analyzed:

* Top-rated products
* Rating distribution
* Relationship between ratings and reviews

### Visualization:

* Scatter plots
* Histograms

### Insight:

Some products with massive reviews still have average ratings.

---

# 5️⃣ Correlation Analysis

Correlation was analyzed between:

* Price
* Discount
* Ratings
* Review count

### Visualization:

* Heatmap

### Insight:

Weak correlation exists between discounts and product ratings.

---


# 🔍 Key Insights

## 📌 Business Insights

### ✅ Electronics dominate the marketplace

Most products belong to electronics-related categories.

### ✅ High discounts are common

Many products offer discounts greater than 40%.

### ✅ Ratings are mostly positive

Most products maintain ratings above 4.0.

### ✅ Reviews impact trust

Products with higher review counts generally attract more buyers.

### ✅ Affordable products dominate

The majority of products fall into budget-friendly price ranges.

---

# 📉 Challenges Faced

During the project, several real-world challenges were encountered:

* Missing values
* Inconsistent data formatting
* Currency symbols in price columns
* Percentage symbols in discount columns
* Incorrect datatypes
* Large text fields

These challenges helped improve data-cleaning and preprocessing skills.

---

# 🎯 Skills Gained From This Project

This project helped improve:

✅ Data Cleaning
✅ Exploratory Data Analysis
✅ Data Visualization
✅ Pandas Operations
✅ Business Analytics
✅ Problem Solving
✅ GitHub Project Structuring

---

# 📚 Important Pandas Functions Used

```python
head()
info()
describe()
groupby()
value_counts()
sort_values()
astype()
isnull()
dropna()
```

---

# 📊 Visualization Techniques Used

* Bar Plot
* Histogram
* Heatmap
* Scatter Plot
* Count Plot
* Distribution Plot

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/your-username/Amazon_Product_Analysis.git
```

---

## Move Into Project Folder

```bash
cd Amazon_Product_Analysis
```

---

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Run Jupyter Notebook

```bash
jupyter notebook
```

---

# ▶️ How To Run Project

1. Open Jupyter Notebook
2. Open `amazon_analysis.ipynb`
3. Run all cells step-by-step
4. View visualizations and insights

---

# 📌 Future Improvements

Future enhancements planned:

* Interactive dashboard using Streamlit
* Machine learning recommendation system
* Sentiment analysis on reviews
* Power BI dashboard
* SQL database integration
* Real-time Amazon product tracking

---

# 💡 Learning Outcomes

Through this project, I learned:

* How to clean messy real-world datasets
* How businesses analyze product data
* How to create meaningful visualizations
* How to generate insights from raw data
* How to structure a professional GitHub project

---

# 🤝 Contribution

Contributions and suggestions are welcome.

Feel free to fork this repository and improve the project.

---

# 📜 License

This project is licensed under the MIT License.

---

# 🙋 Author

## Your Name

ER. Ankit Pawar
Aspiring AI/ML & Data Science Developer

---

# ⭐ If You Like This Project

If you found this project useful:

⭐ Star this repository
⭐ Fork the project
⭐ Share feedback

---
