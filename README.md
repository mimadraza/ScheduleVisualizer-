# 📘 BSCS Course Schedule Visualizer

A Dash web app to **visualize BSCS courses** from the IBA Undergraduate Schedule in a weekly calendar view.  
Data is **scraped live from a Google Sheet** and updated automatically by a background process.

---

## 📁 Project Structure

```
.
├── app.py                     # 🎨 Main Dash app – renders the calendar UI
├── scrape_loop.py            # 🔁 Background scraper – updates the schedule CSV periodically
├── BSCS_Course_Schedule.csv  # 📄 Auto-generated CSV with the latest BSCS schedule data
├── requirements.txt          # 📦 Python dependencies
└── README.md                 # 📘 Project documentation
```

---

## 🚀 Getting Started

### 1. 🔧 Clone the Project & Set Up a Virtual Environment

```bash
git clone https://github.com/yourname/bscs-visualizer.git
cd bscs-visualizer

python -m venv venv
# Activate virtual environment
source venv/bin/activate           # For Linux/macOS
venv\Scripts\activate              # For Windows

# Install dependencies
pip install -r requirements.txt
```

---

### 2. 🧼 Start the Data Scraper (in a Separate Terminal)

```bash
python scrape_loop.py
```

- This script runs **continuously in the background**.
- It updates `BSCS_Course_Schedule.csv` every **10 minutes** by fetching the latest data from the Google Sheet.
- Keep this terminal **open** or run it with `nohup`, `tmux`, or a background task runner.

---

### 3. 📊 Launch the Dash App

In **another terminal**, run:

```bash
python app.py
```

Then open your browser and visit:  
👉 [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## ✨ Features

- 🗓️ Weekly calendar layout
- 🕒 Time slot filter
- 🔍 Real-time search (by course, teacher, room, etc.)
- 🔁 Background data refresh from Google Sheets
- ⚡ Fast and responsive UI

---

## 📦 Requirements

Installed via `requirements.txt`:

```
dash==2.14.2
dash-bootstrap-components==1.5.0
pandas==2.2.1
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📎 Notes

- Ensure the Google Sheet is **shared publicly** or set to **"Anyone with the link can view"**.
- The scraper and app are **decoupled** — you do **not** need to restart the app after every update.
- You can change the scrape interval in `scrape_loop.py` by modifying:  
  `time.sleep(600)` → value in seconds

---

## 🙌 Credits

Created by [Your Name] — powered by [Dash](https://dash.plotly.com/), [Pandas](https://pandas.pydata.org/), and Google Sheets.

---
