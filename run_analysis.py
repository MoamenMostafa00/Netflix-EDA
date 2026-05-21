import sys
import os

# Add src/ to Python's search path so we can import our modules
# Without this, Python wouldn't know where data_loader.py is
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data_loader import load_data, print_overview
from data_cleaner import clean_data
from analysis import (
    q1_content_growth,
    q2_type_split,
    q3_top_countries,
    q4_content_ratings,
    q5_top_genres,
    q6_movie_durations,
    q7_rating_by_type,
    q8_top_directors,
)
from visualizations import run_all


def main():
    print()
    print()
    print("""╔══════════════════════════════════════════════════════╗
║   NETFLIX CONTENT ANALYSIS                           ║
║   Exploratory Data Analysis                          ║
╚══════════════════════════════════════════════════════╝""")

    # Loading data
    print("\n\n━━━  STEP 1 of 4: Load Data  ━━━━━━━━━━━━━━━━━━━━━━━━━━")
    df_raw = load_data("data/netflix_titles.csv")
    print_overview(df_raw)

    # CLeaning data
    print("\n\n━━━  STEP 2 of 4: Clean Data  ━━━━━━━━━━━━━━━━━━━━━━━━━")
    df = clean_data(df_raw)

    # Analysing data
    print("\n\n━━━  STEP 3 of 4: Analyze — Answer Business Questions  ━━")

    analyses = {
        "content_growth":  q1_content_growth(df),
        "type_split":      q2_type_split(df),
        "top_countries":   q3_top_countries(df),
        "content_ratings": q4_content_ratings(df),
        "top_genres":      q5_top_genres(df),
        "movie_durations": q6_movie_durations(df),
        "rating_by_type":  q7_rating_by_type(df),
        "top_directors":   q8_top_directors(df),
    }

    # Visualizing and drawing charts
    print("\n\n━━━  STEP 4 of 4: Generate Charts  ━━━━━━━━━━━━━━━━━━━━━")
    run_all(analyses)

    # Summarize findings
    print()
    print("""╔══════════════════════════════════════════════════════════╗
║   ANALYSIS COMPLETE                                      ║
╠══════════════════════════════════════════════════════════╣""")

    type_split  = analyses["type_split"]
    total       = type_split.sum()
    movie_count = type_split.get("Movie", 0)
    show_count  = type_split.get("TV Show", 0)
    top_genre   = analyses["top_genres"].index[0]
    top_country = analyses["top_countries"].index[0]
    avg_min     = analyses["movie_durations"].mean()
    peak_year   = int(analyses["content_growth"].idxmax())

    print(f"""║                                                          ║
║   Dataset:    {f'{total:,} titles':<42} ║
║   Movies:     {f'{movie_count:,} ({movie_count/total*100:.0f}%)':<42} ║
║   TV Shows:   {f'{show_count:,} ({show_count/total*100:.0f}%)':<42} ║
║   Top genre:  {f'{top_genre:<20}':<42} ║
║   Top country: {f'{top_country:<20}':<42}║
║   Avg movie:  {f'{avg_min:.0f} minutes':<42} ║
║   Peak year:  {f'{peak_year} (most titles added)':<42} ║
║                                                          ║
║   Charts saved to:  outputs/  (8 PNG files)              ║
║                                                          ║
║   Technologies: Python · pandas · Matplotlib · Seaborn   ║
╚══════════════════════════════════════════════════════════╝""")
    print()


if __name__ == "__main__":
    main()