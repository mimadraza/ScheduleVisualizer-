import pandas as pd

# Google Sheets direct CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/1Bqg8jvcxhZ7xUEF5hBRwl8ZqxxxxtjqQnuy3HirL6fA/export?format=csv&gid=1401287543"

# Read the CSV but skip the first 5 rows (adjust if needed)
df_raw = pd.read_csv(sheet_url, skiprows=5)

# Check columns first
print("Columns:", df_raw.columns.tolist())

# Rename columns (must match actual structure)
df_raw.columns = [
    "Timings", "MonWed_Course", "MonWed_ClassProgram", "MonWed_Room", "MonWed_ClassNo", "MonWed_Teacher",
    "TueThu_Course", "TueThu_ClassProgram", "TueThu_Room", "TueThu_ClassNo", "TueThu_Teacher",
    "FriSat_Course", "FriSat_ClassProgram", "FriSat_Room", "FriSat_ClassNo", "FriSat_Teacher", "Extra"
]

# Forward fill timings
df_raw["Timings"] = df_raw["Timings"].ffill()

# Filter for BSCS
bscs_df = df_raw[
    df_raw["MonWed_ClassProgram"].astype(str).str.contains("BSCS", na=False) |
    df_raw["TueThu_ClassProgram"].astype(str).str.contains("BSCS", na=False) |
    df_raw["FriSat_ClassProgram"].astype(str).str.contains("BSCS", na=False)
]

# Save to CSV
bscs_df.to_csv("BSCS_Course_Schedule.csv", index=False)
print("✅ Saved as BSCS_Course_Schedule.csv")
