import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    print("\n\n→  Cleaning Dataset")
    print("─" * 40)

    df = _fill_missing_values(df)
    df = _convert_date_added(df)
    df = _extract_duration_minutes(df)

    print(f"\n\n→  Cleaning complete.")
    print("─" * 40)
    print(f"\n  ✓ Final shape: {df.shape}")
    print(f"\n  ✓ Columns now: {list(df.columns)}")

    return df


def _fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    print("\n[1/3] Filling missing values:")
    before_rows = len(df)

    # Fill text columns with placeholder strings
    fill_map = {
        "director":   "Unknown Director",
        "cast":       "Unknown Cast",
        "country":    "Unknown",
        "rating":     "Not Rated",
        "duration":   "Unknown",
    }

    for col, fill_value in fill_map.items():
        if col in df.columns:
            n_missing = df[col].isnull().sum()
            if n_missing > 0:
                df[col] = df[col].fillna(fill_value)
                print(f"   ✓ {col}: filled {n_missing} missing with '{fill_value}'")

    # Drop rows where date_added is missing
    if "date_added" in df.columns:
        n_missing_date = df["date_added"].isnull().sum()
        if n_missing_date > 0:
            df = df.dropna(subset=["date_added"])
            print(f"   ✓ 'date_added': dropped {n_missing_date} rows with missing dates")

    after_rows = len(df)
    print(f"   ✓ Rows: {before_rows:,} → {after_rows:,} (removed {before_rows - after_rows})")

    return df


def _convert_date_added(df: pd.DataFrame) -> pd.DataFrame:
    print("\n[2/3] Converting date column:")

    if "date_added" not in df.columns:
        print("   →  'date_added' column not found. Skipping.")
        return df

    # Strip extra whitespace from the strings first
    df["date_added"] = df["date_added"].str.strip()

    # Convert to datetime
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # Extract just the year as an integer column
    # .dt.year accesses the year from a datetime column
    df["year_added"] = df["date_added"].dt.year.astype("Int64")
    # Int64 (capital I) supports missing values (NaN); int64 doesn't

    valid = df["year_added"].notna().sum()
    print(f"   ✓ 'date_added' converted to datetime")
    print(f"   ✓ 'year_added' column created ({valid:,} valid values)")

    # Show range of years as a sanity check
    min_year = df["year_added"].min()
    max_year = df["year_added"].max()
    print(f"   ✓ Year range: {min_year} – {max_year}")

    return df


def _extract_duration_minutes(df: pd.DataFrame) -> pd.DataFrame:
    print("\n[3/3] Extracting numeric duration...")

    if "duration" not in df.columns or "type" not in df.columns:
        print("   ⚠  Required columns missing. Skipping.")
        return df

    # Extract the number from the duration string
    df["duration_value"] = (
        df["duration"]
        .str.extract(r"(\d+)")   # grab first group of digits
        [0]                       # extract() returns a DataFrame; [0] gets the first column
        .astype(float)            # convert from string "90" to number 90.0
    )

    # Split into separate columns for movies vs TV shows
    movie_mask = df["type"] == "Movie"
    show_mask  = df["type"] == "TV Show"

    df.loc[movie_mask, "movie_minutes"] = df.loc[movie_mask, "duration_value"]
    df.loc[show_mask,  "tv_seasons"]    = df.loc[show_mask,  "duration_value"]

    n_movies = movie_mask.sum()
    n_shows  = show_mask.sum()
    print(f"   ✓ 'movie_minutes' extracted for {n_movies:,} movies")
    print(f"   ✓ 'tv_seasons' extracted for {n_shows:,} TV shows")

    return df


def get_genres_series(df: pd.DataFrame) -> pd.Series:
    genre_series = (
        df["listed_in"]
        .str.split(", ")       # split "Drama, Comedy" into ["Drama", "Comedy"]
        .explode()             # one genre per row
        .str.strip()           # remove leading/trailing spaces
        .value_counts()        # count each genre
    )
    return genre_series