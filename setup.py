import os
import sys
import urllib.request

print()
print()
print("=" * 56)
print("  Netflix EDA - Project Setup")
print("=" * 56)


# Create folders
print("\n\n  ── Step 1: Creating project folders ──────────────────\n")

folders = ["data", "src", "outputs", "docs"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"   ✓ {folder}/")


# Download dataset
print("\n\n  ── Step 2: Downloading Netflix dataset ───────────────\n")

DATA_PATH = os.path.join("data", "netflix_titles.csv")

DATASET_URL = (
    "https://raw.githubusercontent.com/dsrscientist/"
    "dataset1/master/netflix_titles.csv"
)

if os.path.exists(DATA_PATH):
    print(f"   ✓ Dataset already exists at '{DATA_PATH}'. Skipping.")
else:
    try:
        print(f"   Downloading from public mirror...")
        urllib.request.urlretrieve(DATASET_URL, DATA_PATH)
        print(f"   ✓ Saved to '{DATA_PATH}'")
    except Exception as e:
        print(f"   ✗ Could not auto-download: {e}")
        print()
        print("""   ── Manual download instructions ──────────────────
        1. Go to: https://www.kaggle.com/datasets/shivamb/netflix-shows
        2. Click 'Download' (free Kaggle account needed)
        3. Unzip and place 'netflix_titles.csv' in the data/ folder
        ──────────────────────────────────────────────────""")


# Check if necessary libraries are installed
print("\n\n  ── Step 3: Checking required libraries ───────────────\n")

libraries = ["pandas", "numpy", "matplotlib", "seaborn"]
all_good = True

for lib in libraries:
    try:
        __import__(lib)
        print(f"   ✓ {lib} - installed")
    except ImportError:
        print(f"   ✗ {lib} - NOT FOUND  →  run: pip install {lib}")
        all_good = False


# Checking dataset
if os.path.exists(DATA_PATH) and all_good:
    print("\n\n  ── Step 4: Quick dataset preview ─────────────────────\n")
    try:
        import pandas as pd
        df = pd.read_csv(DATA_PATH)
        print(f"""   ✓ Loaded successfully
   ✓ Shape: {df.shape[0]:,} rows × {df.shape[1]} columns
   ✓ Columns: {list(df.columns)}""")
    except Exception as e:
        print(f"     Could not preview: {e}")


# Summary
print()
print()
print("=" * 56)

if all_good and os.path.exists(DATA_PATH):
    print("   ✓ Setup complete! You're ready to go!")
    print()
    print("""     Run the full analysis:
      → python run_analysis.py""")
    print()
    print("""     Or open the interactive notebook:
      → jupyter notebook""")
else:
    print("""     Setup finished with issues above." 
      → Fix the errors, then run this script again.""")

print("=" * 56)
print()
print()