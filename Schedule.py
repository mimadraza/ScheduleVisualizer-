import pandas as pd
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Load the BSCS course schedule
df = pd.read_csv("BSCS_Course_Schedule.csv")
df["Timings"] = df["Timings"].ffill()

# Format course info
def format_course_info(course, program, room, classno, teacher):
    return f"**{course}** ({program})  \n{room}, Class#: {classno}  \nInstructor: {teacher}"

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
schedule = {day: [] for day in days}

# Assign courses to days
for _, row in df.iterrows():
    if pd.notna(row["MonWed_Course"]):
        for day in ["Monday", "Wednesday"]:
            schedule[day].append((row["Timings"], format_course_info(
                row["MonWed_Course"], row["MonWed_ClassProgram"],
                row["MonWed_Room"], row["MonWed_ClassNo"], row["MonWed_Teacher"]
            )))
    if pd.notna(row["TueThu_Course"]):
        for day in ["Tuesday", "Thursday"]:
            schedule[day].append((row["Timings"], format_course_info(
                row["TueThu_Course"], row["TueThu_ClassProgram"],
                row["TueThu_Room"], row["TueThu_ClassNo"], row["TueThu_Teacher"]
            )))
    if pd.notna(row["FriSat_Course"]):
        for day in ["Friday", "Saturday"]:
            schedule[day].append((row["Timings"], format_course_info(
                row["FriSat_Course"], row["FriSat_ClassProgram"],
                row["FriSat_Room"], row["FriSat_ClassNo"], row["FriSat_Teacher"]
            )))

# Get unique time options
time_options = sorted({t for day in schedule.values() for t, _ in day if pd.notna(t)})

# Dash App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.H2("BSCS Weekly Course Calendar", className="my-4 text-center"),

    # Filter section
    dbc.Row([
        dbc.Col([
            html.Label("🕒 Filter by Time", className="fw-bold"),
            dcc.Dropdown(
                options=[{"label": t, "value": t} for t in time_options],
                id="time-filter",
                placeholder="Select a time slot...",
                clearable=True
            )
        ], width=4),
        dbc.Col([
            html.Label("🔍 Search", className="fw-bold"),
            dcc.Input(
                id="search-input",
                type="text",
                placeholder="Search course, teacher, room...",
                debounce=False,  # ✅ Live sync as you type
                className="form-control"
            )
        ], width=8)
    ], className="mb-4"),

    # Calendar display
    dbc.Row(id="calendar-view")
], fluid=True)

# Card generator
def generate_day_column(day, courses):
    return dbc.Col([
        html.H5(day, className="text-center text-primary"),
        html.Div([
            dbc.Card([
                dbc.CardBody([
                    html.H6(time, className="card-title"),
                    dcc.Markdown(info, className="card-text", style={"fontSize": "0.9em"})
                ])
            ], className="mb-3 shadow-sm")
            for time, info in courses
        ])
    ], style={"minWidth": "200px"})

# Callback with both filters
@app.callback(
    Output("calendar-view", "children"),
    Input("time-filter", "value"),
    Input("search-input", "value")
)
def update_calendar(selected_time, search_text):
    search_text = (search_text or "").lower()

    filtered = {
        day: [
            (t, info) for t, info in schedule[day]
            if (not selected_time or t == selected_time) and (search_text in info.lower())
        ]
        for day in days
    }

    return [generate_day_column(day, filtered[day]) for day in days]

# Run
if __name__ == "__main__":
    app.run(debug=True)
