import pandas as pd

# Read the CSV file
df = pd.read_csv('crashdata2022-present.csv')

# Filter the rows where HitAndRunFlag is True
hit_and_run_df = df[df['HitAndRunFlag'] == 'True']  # Assuming the flag is stored as a string

# Output to hitandrun.csv
hit_and_run_df.to_csv('hitandrun.csv', index=False)