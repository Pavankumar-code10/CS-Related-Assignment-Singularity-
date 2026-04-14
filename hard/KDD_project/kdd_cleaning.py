import pandas as pd

print("Script started")


df = pd.read_csv("stars_raw.csv")
print("\nData loaded successfully")
print(df.head())

df = df.drop_duplicates()

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

print("\nMissing values handled")


if 'temperature' in df.columns:
    df = df[df['temperature'] > 0]

if 'mass' in df.columns:
    df = df[df['mass'] > 0]

print("\nInvalid values removed")


df = df.reset_index(drop=True)

df.to_csv("stars_cleaned.csv", index=False)

print("\nCleaning completed successfully!")
print("Rows after cleaning:", len(df))
