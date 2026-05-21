# Netflix content analysis

> **Project type** | Exploratory Data Analysis & Visualization  
> **Time to Complete:** 10-12 hours  
> **Stack:** Python · Pandas · Matplotlib · Seaborn  

---

## 📌 What's the purpose of this project

The analysis of the **Netflix Movies and TV Shows dataset**, a real dataset of 8,800+ titles, to answer business questions using data.

This is crucial for business operations and descisions, as data often leads the path to where investments occur, which usually looks like this:
load data → clean it → ask questions → answer them with charts → tell a story.

---

## 🎯 Questions this project answers

In order to analyse which path the business needs to invest in, we need to ask several questions that will end up telling us a story, the following tables showcases these questions, and which technique we'll use to assess such data.

| # | Question | Chart Type |
|---|----------|-----------|
| 1 | How much content has Netflix added each year? | Line chart |
| 2 | What is the split between Movies and TV Shows? | Pie + bar chart |
| 3 | Which countries produce the most Netflix content? | Horizontal bar chart |
| 4 | What are the most common content ratings? | Bar chart |
| 5 | Which genres dominate the platform? | Bar chart |
| 6 | How long are movies on Netflix? | Histogram |
| 7 | What does content look like by rating AND type? | Grouped bar chart |
| 8 | Which directors appear most? | Bar chart |

---

## 🧠 Skills utalized in this project

| Skill | Use case |
|-------|--------------------------|
| `pandas` - loading data | Read a CSV file and explore it |
| `pandas` - cleaning | Fix missing values, wrong types, messy strings |
| `pandas` - grouping | Group by category and count/summarize |
| `pandas` - filtering | Select rows that match a condition |
| `matplotlib` | Create and style any chart from scratch |
| `seaborn` | Create beautiful statistical charts in fewer lines |
| Data storytelling | Turn numbers into insight sentences |

---

## 🗂️ Project structure

```
Netflix-EDA/
│
├── data/
│   └── netflix_titles.csv          ← dataset 
│
├── src/
│   ├── data_loader.py              ← load & inspect the dataset
│   ├── data_cleaner.py             ← fix missing values, fix types
│   ├── analysis.py                 ← answer each business question
│   └── visualizations.py           ← all chart functions
│
├── outputs/                        ← all generated charts saved here
|
├── requirements.txt                ← Python libraries needed
├── setup.py                        ← run once to download data & check setup
├── run_analysis.py                 ← run this to execute the full project
└── README.md                       ← this file
```

---

## ⚙️ How to set up and run

### Step 1 - Make sure Python is installed
```bash
python --version
```
Download Python here if needed: https://www.python.org/downloads/

### Step 2 - Get the project files
Clone the github repo to your local machine
```bash
git clone https://github.com/MoamenMostafa00/Netflix-EDA.git
```
Or just download and unzip the folder.

Open the project directory on your terminal 
```bash
cd beginner-netflix-eda
```

### Step 3 - Install the required libraries
```bash
pip install -r requirements.txt
# This takes about 1-2 minutes
```

### Step 4 - Run setup
```bash
python setup.py
```
This makes sure the dataset is installed, all necessary directories and files exist, and all necessary libraries are installed
### Step 5 - Run the full analysis
```bash
python run_analysis.py
```
This runs everything from start to finish and saves 8 charts to the `outputs/` folder.

### Step 6 - Open the charts
Go into the `outputs/` folder and open any `.png` file to see your charts.

---

## 📊 What the outputs look Like

After running, you'll have:
```
outputs/
├── 01_content_growth.png        ← Netflix content added per year
├── 02_type_split.png            ← Movies vs TV Shows breakdown
├── 03_top_countries.png         ← Countries producing most content
├── 04_content_ratings.png       ← G, PG, TV-MA, etc.
├── 05_top_genres.png            ← Drama, Comedy, Documentary, etc.
├── 06_movie_durations.png       ← How long are Netflix movies?
├── 07_rating_by_type.png        ← Rating breakdown by content type
└── 08_top_directors.png         ← Most prolific Netflix directors
```

---

## 🛠️ Technologies & tools

| Tool | Version | Why We Use It |
|------|---------|---------------|
| Python | 3.8+ | The programming language |
| pandas | 2.x | Load, clean, and manipulate data tables |
| NumPy | 1.x | Numerical operations (used behind the scenes) |
| Matplotlib | 3.x | The foundation of all Python charts |
| Seaborn | 0.13 | Beautiful statistical charts built on Matplotlib |
| Jupyter | Latest | Run code interactively, see output inline |

---

## 💼 Learning outcomes from this project

- ✅ Load and explore a real-world dataset independently
- ✅ Identify and fix data quality problems
- ✅ Ask meaningful business questions and answer them with data
- ✅ Create clear, well-labeled charts
- ✅ Write clean, organized Python code
- ✅ Document my work so it's readable 

## 📈 Future improvements 

- ⚡Swap the static CSV for the Netflix API or a live scraper so the analysis always reflects current data
- ⚡Replace the static charts with an interactive dashboard
- ⚡Schedule the analysis to re-run automatically when new data is available
- ⚡Enrich it with IMDB ratings and scores for more accurate results