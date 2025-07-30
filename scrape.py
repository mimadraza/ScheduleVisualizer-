import time
import pandas as pd

def run_scraper():
    try:
        print("🔄 Fetching updated BSCS schedule...")
        # Google Sheets CSV export link
        sheet_url = "https://docs.google.com/spreadsheets/d/1Bqg8jvcxhZ7xUEF5hBRwl8ZqxxxxtjqQnuy3HirL6fA/export?format=csv&gid=1401287543"

        # Read and process
        df_raw = pd.read_csv(sheet_url, skiprows=5)
        df_raw.columns = [
            "Timings", "MonWed_Course", "MonWed_ClassProgram", "MonWed_Room", "MonWed_ClassNo", "MonWed_Teacher",
            "TueThu_Course", "TueThu_ClassProgram", "TueThu_Room", "TueThu_ClassNo", "TueThu_Teacher",
            "FriSat_Course", "FriSat_ClassProgram", "FriSat_Room", "FriSat_ClassNo", "FriSat_Teacher", "Extra"
        ]
        df_raw["Timings"] = df_raw["Timings"].ffill()

        bscs_df = df_raw[
            df_raw["MonWed_ClassProgram"].astype(str).str.contains("BSCS", na=False) |
            df_raw["TueThu_ClassProgram"].astype(str).str.contains("BSCS", na=False) |
            df_raw["FriSat_ClassProgram"].astype(str).str.contains("BSCS", na=False)
        ]

        bscs_df.to_csv("BSCS_Course_Schedule.csv", index=False)
        print("✅ Schedule updated and saved.")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# Run forever
if __name__ == "__main__":
    while True:
        run_scraper()
        time.sleep(600)  # 600 seconds = 10 minutes
