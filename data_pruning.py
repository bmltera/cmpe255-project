import pandas as pd

# Read the CSV file
df = pd.read_csv('policecalls2023.csv')

# Filter the rows where CALL_TYPE equals "NMISDEMEANOR HIT AND RUN"
filtered_df = df[df['CALL_TYPE'] == 'MISDEMEANOR HIT AND RUN']

# Output to misdemeanor.csv
filtered_df.to_csv('misdemeanor.csv', index=False)