import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sb
import pandas as pd
import numpy as np
import os

# Global styles
# Fixate all colours and measurments for sleek excution and consistent design across all charts.
sb.set_theme(style="darkgrid", palette="muted")

plt.rcParams.update({
    "figure.facecolor": "#1a1a1a",
    "axes.facecolor":   "#1a1a1a",
    "axes.edgecolor":   "#444444",
    "axes.labelcolor":  "#cccccc",
    "xtick.color":      "#cccccc",
    "ytick.color":      "#cccccc",
    "text.color":       "#eeeeee",
    "grid.color":       "#333333",
    "grid.linewidth":   0.6,
    "figure.dpi":       120,
})

# Main colour and palette for charts
NETFLIX_RED = "#E50914"
PALETTE = ["#E50914", "#F5F5F1", "#831010", "#B20710", "#ff6b6b", "#ffd93d"]

OUTPUT_DIR = "outputs"


def _save(fig: plt.Figure, filename: str) -> None:
    """Save figure to outputs/ and close it to free memory."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"    ✓ Saved → {path}")

# Plot 1: Content growth per year:
# Line chart with shaded area:
# X-axis: year added, Y-axis: count of titles added that year
def plot_content_growth(yearly_counts: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(12, 5))

    years  = yearly_counts.index.astype(int)
    counts = yearly_counts.values

    # Main line
    ax.plot(years, counts, color=NETFLIX_RED, linewidth=2.5, marker="o",
            markersize=5, markerfacecolor="white", zorder=3)

    # Shaded area under the line
    ax.fill_between(years, counts, alpha=0.15, color=NETFLIX_RED)

    # Marking peak year
    peak_year  = years[counts.argmax()]
    peak_count = counts.max()
    ax.annotate(
        f"Peak: {peak_count:,} titles\n({peak_year})",
        xy=(peak_year, peak_count),
        xytext=(peak_year - 1.5, peak_count - 3),
        arrowprops=dict(arrowstyle="->", color="white", lw=1.5),
        color="white", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#222222", edgecolor="#444444")
    )

    # Set titles and labels for graph
    ax.set_title("Netflix Content Added Per Year", fontsize=15, fontweight="bold",
                 color="white", pad=15)
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Number of Titles Added", fontsize=11)
    
    # Formatting axes limits
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xlim(years.min() - 0.5, years.max() + 0.5)
    ax.set_ylim(0, peak_count * 1.15)

    _save(fig, "01_content_growth.png")


# Plot 2: Content type (Movie vs TV Show):
# Pie chart & Bar chart
def plot_type_split(type_counts: pd.Series) -> None:
    fig, (ax_pie, ax_bar) = plt.subplots(1, 2, figsize=(12, 5))

    colors = [NETFLIX_RED, "#F5F5F1"]
    labels = type_counts.index.tolist()
    values = type_counts.values

    # Pie chart
    wedges, texts, autotexts = ax_pie.pie(
        values,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",      
        startangle=90,           
        wedgeprops=dict(edgecolor="#1a1a1a", linewidth=2)
    )
    for text in texts:
        text.set_color("white")
    for autotext in autotexts:
        autotext.set_color("Black")
        autotext.set_fontsize(12)
        autotext.set_fontweight("bold")

    ax_pie.set_title("Content Type Split", fontsize=13, fontweight="bold",
                     color="white", pad=12)

    # Bar chart
    bars = ax_bar.bar(labels, values, color=colors, edgecolor="#1a1a1a",
                      linewidth=1.5, width=0.5)
    padding = 0.02 * max(values)

    # Adding bar values
    for bar, val in zip(bars, values):
        ax_bar.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + padding,
            f"{val:,}",
            ha="center", va="bottom", fontsize=11, fontweight="bold", color="white"
        )

    # Set titles, labels and formatting
    ax_bar.set_ylim(0, max(values) * 1.12)
    ax_bar.set_title("Movies vs TV Shows (Count)", fontsize=13, fontweight="bold",
                     color="white", pad=12)
    ax_bar.set_ylabel("Number of Titles")
    ax_bar.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    plt.tight_layout()

    _save(fig, "02_type_split.png")


# Plot 3: Top countries producing content:
# Horizontal bar chart
# X-axis: count of titles, Y-axis: country names
def plot_top_countries(country_counts: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(10, 7))

    # Reverse so highest value is at the top
    data = country_counts.sort_values(ascending=True)

    colors = [NETFLIX_RED if i == len(data) - 1 else "#555555"
              for i in range(len(data))]

    bars = ax.barh(data.index, data.values, color=colors, edgecolor="none", height=0.7)
    padding = 0.02 * max(data.values)

    # Add value labels
    for bar, val in zip(bars, data.values):
        ax.text(
            bar.get_width() + padding, bar.get_y() + bar.get_height() / 2,
            f"{val:,}",
            va="center", ha="left", fontsize=9, color="#aaaaaa", fontweight="bold"
        )

    # Set titles, labels and formatting
    ax.set_title("Top 15 Countries by Number of Netflix Titles",
                 fontsize=14, fontweight="bold", color="white", pad=15)
    ax.set_xlabel("Number of Titles")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    _save(fig, "03_top_countries.png")


# Plot 4: Content ratings distribution:
# Vertical bar chart 
# X-axis: with ratings, Y-axis: count
def plot_content_ratings(rating_counts: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(11, 5))

    colors = [NETFLIX_RED if i == 0 else "#555555" for i in range(len(rating_counts))]
    bars = ax.bar(rating_counts.index, rating_counts.values,
                  color=colors, edgecolor="none", width=0.7)
    
    padding = 0.02 * max(rating_counts.values)

    # Add value labels
    for bar, val in zip(bars, rating_counts.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + padding,
            f"{val:,}",
            ha="center", va="bottom", fontsize=9, color="white"
        )

    # Average line
    avg = rating_counts.mean()
    ax.axhline(avg, color="#ffd93d", linestyle="--", linewidth=1.2, alpha=0.8)
    ax.text(len(rating_counts) - 0.5, avg + padding, f"avg {avg:.0f}",
            color="#ffd93d", fontsize=8, ha="right")
    
    # Set titles, labels and formatting
    ax.set_ylim(0, max(rating_counts.values) * 1.12)
    ax.set_title("Netflix Content by Rating", fontsize=14, fontweight="bold",
                 color="white", pad=15)
    ax.set_xlabel("Content Rating")
    ax.set_ylabel("Number of Titles")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    plt.xticks(rotation=20, ha="right")

    _save(fig, "04_content_ratings.png")


# Plot 5: Top genres:
# Horizontal bar chart
# X-axis: count of titles, Y-axis: genre names
def plot_top_genres(genre_counts: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(10, 7))

    # Reverse so highest value is at the top
    data = genre_counts.sort_values(ascending=True)

    # Build a gradient from gray → red
    n = len(data)
    reds = plt.cm.Reds(np.linspace(0.3, 0.9, n))

    bars = ax.barh(data.index, data.values, color=reds, edgecolor="none", height=0.75)
    padding = 0.02 * max(data.values)

    # Add value labels    
    for bar, val in zip(bars, data.values):
        ax.text(
            bar.get_width() + padding, bar.get_y() + bar.get_height() / 2,
            f"{val:,}",
            va="center", ha="left", fontsize=9, color="#aaaaaa", fontweight="bold"
        )

    # Set titles, labels and formatting
    ax.set_title("Top 15 Netflix Genres", fontsize=14, fontweight="bold",
                 color="white", pad=15)
    ax.set_xlabel("Number of Titles")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    _save(fig, "05_top_genres.png")


# Plot 6: Movie durations distribution:
# Histogram with KDE line
# X-axis: duration in minutes, Y-axis: count of movies in each bin
def plot_movie_durations(duration_series: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(11, 5))

    # Filter extreme outliers for cleaner chart (less than 10 min or more than 250 min)
    filtered = duration_series[(duration_series >= 10) & (duration_series <= 250)]

    # Histogram bars
    ax.hist(filtered, bins=40, color=NETFLIX_RED, alpha=0.7,
            edgecolor="#1a1a1a", linewidth=0.5)

    # Vertical lines for key statistics
    mean_val   = filtered.mean()
    median_val = filtered.median()

    # Set titles, labels and formatting
    ax.axvline(mean_val,   color="#ffd93d", linestyle="--", linewidth=1.5,
               label=f"Mean: {mean_val:.0f} min")
    ax.axvline(median_val, color="#6bcb77", linestyle="-",  linewidth=1.5,
               label=f"Median: {median_val:.0f} min")

    ax.legend(fontsize=10, facecolor="#222", edgecolor="#444", labelcolor="white")
    ax.set_title("Distribution of Netflix Movie Durations",
                 fontsize=14, fontweight="bold", color="white", pad=15)
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of Movies")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    _save(fig, "06_movie_durations.png")


# Plot 7: Content rating by type:
# Grouped bar chart
# X-axis: content ratings, Y-axis: count of titles, bars grouped by Movie vs TV Show
def plot_rating_by_type(crosstab: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 5))

    x = range(len(crosstab))
    width = 0.4

    # Two bars per rating: one for Movie, one for TV Show
    cols = crosstab.columns.tolist()
    colors_list = [NETFLIX_RED, "#F5F5F1"]

    # Creating offsets to separate bars
    for i, (col, color) in enumerate(zip(cols, colors_list)):
        offset = (i - 0.5) * width
        bars = ax.bar(
            [xi + offset for xi in x],
            crosstab[col],
            width=width,
            color=color,
            label=col,
            edgecolor="#1a1a1a",
            linewidth=0.8
        )

    # Set titles, labels and formatting
    ax.set_xticks(list(x))
    ax.set_xticklabels(crosstab.index, rotation=20, ha="right")
    ax.legend(fontsize=10, facecolor="#222", edgecolor="#444", labelcolor="white")
    ax.set_title("Content Rating by Type (Movie vs TV Show)",
                 fontsize=14, fontweight="bold", color="white", pad=15)
    ax.set_ylabel("Number of Titles")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

    _save(fig, "07_rating_by_type.png")


# Plot 8: Most prolific directors:
# Horizontal bar chart
# X-axis: count of titles, Y-axis: director names
def plot_top_directors(director_counts: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))

    # Reverse so highest value is at the top
    data = director_counts.sort_values(ascending=True)
    colors = [NETFLIX_RED if i == len(data) - 1 else "#555555"
              for i in range(len(data))]

    bars = ax.barh(data.index, data.values, color=colors, edgecolor="none", height=0.65)
    padding = 0.02 * max(data.values)

    # Add value labels 
    for bar, val in zip(bars, data.values):
        ax.text(
            bar.get_width() + padding, bar.get_y() + bar.get_height() / 2,
            str(int(val)),
            va="center", ha="left", fontsize=10, color="#aaaaaa", fontweight="bold"
        )

    # Set titles, labels and formatting
    ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
    ax.set_title("Most Prolific Netflix Directors",
                 fontsize=14, fontweight="bold", color="white", pad=15)
    ax.set_xlabel("Number of Titles")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlim(0, data.max() + 1)

    _save(fig, "08_top_directors.png")


# Running all charts in one call
def run_all(analyses: dict) -> None:
    print("\n→  Generating All Charts")
    print("─" * 40)

    # Mapping keys to their corresponding plotting functions
    chart_functions = {
        "content_growth":  plot_content_growth,
        "type_split":      plot_type_split,
        "top_countries":   plot_top_countries,
        "content_ratings": plot_content_ratings,
        "top_genres":      plot_top_genres,
        "movie_durations": plot_movie_durations,
        "rating_by_type":  plot_rating_by_type,
        "top_directors":   plot_top_directors,
    }

    # Excution cycle for the appropriate analysis function
    for key, func in chart_functions.items():
        if key in analyses:
            print(f"\n   Plotting: {key}...")
            func(analyses[key])

    print(f"\n   → All charts saved to '{OUTPUT_DIR}/'")