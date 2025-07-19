import pandas as pd

df = pd.read_parquet(r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\airport_parking_dataset\final_output.parquet")
df.to_csv(r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\airport_parking_dataset\cleaned_data.csv", index=False)
