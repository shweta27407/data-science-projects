import pandas as pd

# Load your dataset
df = pd.read_csv('/Users/shwetabambal/Documents/myrepos/data-science-/Geo_spatial_Time_Series_Analysis/dataset_10_percent.csv')

# Sample 40% of the data (removing 60%)
reduced_df = df.sample(frac=0.03, random_state=42)  # random_state ensures reproducibility

# Save the reduced dataset
reduced_df.to_csv('/Users/shwetabambal/Documents/myrepos/data-science-/Geo_spatial_Time_Series_Analysis/dataset_3_percent.csv', index=False)