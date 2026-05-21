import pandas as pd

# Analysis 1: How much content has Netflix added each year?
def q1_content_growth(df: pd.DataFrame) -> pd.Series:
    result = (
        df.dropna(subset=["year_added"])   # ignore rows with no year
        .groupby("year_added")             # group by year
        .size()                            # count rows per group
        .sort_index()                      # sort by year (oldest → newest)
    )

    print("\n→ Q1: Content Added Per Year")
    print("─" * 40)
    print()
    for year, count in result.items():
        bar = "████" * int(count / 80)  # scale bar to terminal width
        print(f"   {int(year)}  {count:>5,}  {bar}")

    return result


# Analysis 2: What is the split between Movies and TV Shows?
def q2_type_split(df: pd.DataFrame) -> pd.Series:
    result = df["type"].value_counts()

    print("\n\n→ Q2: Movies vs TV Shows")
    print("─" * 40)
    print()
    total = result.sum()
    for content_type, count in result.items():
        pct = count / total * 100
        print(f"   {content_type:<10}  {count:<6}  ({pct:.1f}%)")

    return result


# Analysis 3: Which countries produce the most Netflix content?
def q3_top_countries(df: pd.DataFrame, top_n: int = 15) -> pd.Series:
    result = (
        df["country"]
        .str.split(", ")         # split multi-country cells
        .explode()               # one country per row
        .str.strip()             # clean up whitespace
        [lambda s: s != "Unknown"]   # exclude our placeholder
        .value_counts()          # count each country
        .head(top_n)             # keep top N
    )

    print(f"\n\n→ Q3: Top {top_n} Countries by Content Count")
    print("─" * 40)
    print()
    for country, count in result.items():
        bar = "█" * int(count / 100)
        print(f"   {country:<30}  {count:>5,}  {bar}")

    return result


# Analysis 4: What are the most common content ratings?
def q4_content_ratings(df: pd.DataFrame) -> pd.Series:
    result = (
        df["rating"]
        .value_counts()
        .head(12)   # Top 12 ratings (removes very rare ones)
    )

    print("\n\n→ Q4: Content Ratings")
    print("─" * 40)
    print()
    for rating, count in result.items():
        bar = "█" * int(count / 100)
        print(f"   {rating:<12}  {count:>5,}  {bar}")

    return result


# Analysis 5: Which genres dominate Netflix?
def q5_top_genres(df: pd.DataFrame, top_n: int = 15) -> pd.Series:
    result = (
        df["listed_in"]
        .str.split(", ")
        .explode()
        .str.strip()
        .value_counts()
        .head(top_n)
    )

    print(f"\n\n→ Q5: Top {top_n} Genres")
    print("─" * 40)
    print()
    for genre, count in result.items():
        bar = "█" * int(count / 80)
        print(f"   {genre:<35}  {count:>8,}  {bar}")

    return result


# Analysis 6: How long are Netflix movies (in minutes)?
def q6_movie_durations(df: pd.DataFrame) -> pd.Series:
    result = (
        df[df["type"] == "Movie"]["movie_minutes"]
        .dropna()
    )

    print(f"\n\n→ Q6: Movie Duration Statistics")
    print("─" * 40)
    print()
    print(f"   Count:   {len(result):,} movies")
    print(f"   Shortest:{result.min():.0f} min")
    print(f"   Longest: {result.max():.0f} min")
    print(f"   Average: {result.mean():.0f} min  ({result.mean()/60:.1f} hours)")
    print(f"   Median:  {result.median():.0f} min")

    return result


# Analysis 7: How do content ratings differ between Movies and TV Shows?
def q7_rating_by_type(df: pd.DataFrame) -> pd.DataFrame:
    result = pd.crosstab(df["rating"], df["type"])

    # Keep only the top 10 most common ratings to keep the chart readable
    top_ratings = df["rating"].value_counts().head(10).index
    result = result.loc[result.index.isin(top_ratings)]
    result = result.sort_values("Movie", ascending=False)

    print(f"\n\n→ Q7: Rating × Type Crosstab (top 10 ratings)")
    print("─" * 40)
    print()
    print(result.to_string())

    return result


# Analysis 8: Which directors have the most titles on Netflix?
def q8_top_directors(df: pd.DataFrame, top_n: int = 12) -> pd.Series:
    result = (
        df["director"]
        .str.split(", ")
        .explode()
        .str.strip()
        [lambda s: s != "Unknown Director"]
        .value_counts()
        .head(top_n)
    )

    print(f"\n\n→ Q8: Top {top_n} Directors by Number of Titles")
    print("─" * 40)
    print()
    for director, count in result.items():
        bar = "██" * count
        print(f"   {director:<35}  {count:>3}  {bar}")

    return result
