import pandas as pd
import csv  # Import the csv module for quoting options

# Read the CSV file
df = pd.read_csv('hit_n_run.csv')

# Filter the rows where HitAndRunFlag is True and CrashDateTime contains '2023'
hit_and_run_2023_df = df[(df['CrashDateTime'].str.contains('2023', na=False))]

# Output to hitnrun_crash_2023.csv with all fields quoted
hit_and_run_2023_df.to_csv('hitnrun_crash_2023.csv', index=False, quoting=csv.QUOTE_ALL)