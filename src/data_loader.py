import pandas as pd
import os


def load_data(filepath: str = "data/netflix_titles.csv") -> pd.DataFrame:
    # Check the file actually exists before trying to load it
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"\n✗ File not found: '{filepath}'\n"
            "  Run 'python setup.py' first to download the dataset."
        )

    # pd.read_csv() reads the file and returns a DataFrame
    df = pd.read_csv(filepath)

    print(f"✓ Dataset loaded from '{filepath}'")
    print(f"  → {df.shape[0]:,} rows (titles)  ×  {df.shape[1]} columns")

    return df


def print_overview(df: pd.DataFrame) -> None:
    """
    Print a complete first-look summary of the dataset.

    This is the very first thing you should do with any new dataset.
    It answers: What do I have? Is anything broken?

    Parameters
    ----------
    df : pd.DataFrame
        The loaded Netflix dataset.
    """

    print("\n" + "═" * 55)
    print("  DATASET OVERVIEW")
    print("═" * 55)


    # Size of dataset
    print(f"\n\n→  Size")
    print("─" * 40)
    print(f"""\n    {df.shape[0]:,} rows  (one per Netflix title)
    {df.shape[1]} columns (properties of each title)""")


    # Columns, names, and data types
    print(f"\n\n→  Columns")
    print("─" * 40)
    print(f"""\n   {'Column':<20}  {'Type':<12}  Description
   {'──────':<20}  {'────':<12}  ───────────""")


    # Human-readable descriptions for each column
    descriptions = {
        "show_id":      "Unique ID for each title",
        "type":         "Movie or TV Show",
        "title":        "Name of the title",
        "director":     "Director name(s)",
        "cast":         "Main actors",
        "country":      "Country of production",
        "date_added":   "When it was added to Netflix",
        "release_year": "Year it was originally released",
        "rating":       "Content rating (PG, TV-MA, etc.)",
        "duration":     "Length in minutes or seasons",
        "listed_in":    "Genres / categories",
        "description":  "Short plot summary",
    }

    for col in df.columns:
        dtype_str = str(df[col].dtype)
        desc = descriptions.get(col, "")
        print(f"   {col:<20}  {dtype_str:<12}  {desc}")


    # Showcasing first 3 rows in the dataset
    print(f"\n\n→  First 3 Rows")
    print("─" * 40)
    print()

    # to_string() avoids line-wrapping on small terminals
    print(df.head(3).to_string())


    # Completing missing vales
    print(f"\n\n→   Missing Values")
    print("─" * 40)
    print()

    missing = df.isnull().sum()
    missing = missing[missing > 0]  # Only show columns that have missing values

    if len(missing) == 0:
        print("   None! The dataset is complete.")
    else:
        print(f"""   {'Column':<20}  {'Missing Count':>15}  {'% of Total':>12}
   {'──────':<20}  {'─────────────':>15}  {'──────────':>12}""")
        for col, count in missing.sort_values(ascending=False).items():
            pct = count / len(df) * 100
            bar = "█" * int(pct / 5)  # Simple text bar chart
            print(f"   {col:<20}  {count:>15,}  {pct:>11.1f}%  {bar}")


    # Overview of unique values in each column
    print(f"\n\n→  Unique Value Counts")
    print("─" * 40)
    print()

    for col in df.columns:
        n = df[col].nunique()
        print(f"   {col:<20}  {n:>6,} unique values")

    print()
    print("\n" + "═" * 60)
