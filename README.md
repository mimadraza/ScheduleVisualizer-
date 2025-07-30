A Dash web app to visualize BSCS courses from the IBA Undergraduate Schedule on a weekly calendar. Data is scraped directly from a Google Sheet and updated regularly by a separate background process.

.
├── app.py                     # Main Dash app – renders the calendar UI
├── scrape_loop.py            # Background scraper – updates BSCS_Course_Schedule.csv periodically
├── BSCS_Course_Schedule.csv  # Auto-generated CSV with latest BSCS schedule data
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

git clone https://github.com/yourname/bscs-visualizer.git
cd bscs-visualizer

1. Clone the project & set up a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt

2. Start the Data Scraper (in a separate terminal)
  python scrape_loop.py
  This runs continuously in the background and updates BSCS_Course_Schedule.csv every 10 minutes by fetching data from the linked Google Sheet.
3. Run the Dash App
  In another terminal:
  python app.py
