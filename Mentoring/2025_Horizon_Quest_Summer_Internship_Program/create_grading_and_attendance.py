import pandas as pd
# Read the Google Sheets data and save it as grades.md and attendance.md
# The Google Sheets URL is provided, and we will read the first 8 rows of the data.
# The first two columns are student names and IDs, and we will extract specific columns for grades and attendance.

# Google Sheets URL
sheet_id = "1bKIpahiKTTU5LCi2HG2-Z8GJ22Xym8_O9hYC2RaY0FE"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
df = pd.read_csv(url)
df = df.head(8)

print(df.shape)

# Read columns 0,1 and 2:9 and save as grades.md
grades_df = df.iloc[:, [0, 1] + list(range(2, 10))]
grades_output_file = "grades.md"
with open(grades_output_file, "w") as f:
    f.write(grades_df.to_markdown())

# Read columns 0,1 and 13:20 and save as attendance.md
attendance_df = df.iloc[:, [0, 1] + list(range(13, 21))]
attendance_output_file = "attendance.md"
with open(attendance_output_file, "w") as f:
    f.write(attendance_df.to_markdown())