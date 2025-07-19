import duckdb
import os

# Path to input Parquet file
parquet_file = r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\airport_parking_dataset\final_output.parquet"

# Output folder for query results
output_folder = r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\Query_Results"
os.makedirs(output_folder, exist_ok=True)

# Load SQL queries from file
with open("queries.sql", "r") as file:
    queries = file.read().split(";")

# Connect to DuckDB
con = duckdb.connect()

# Create a DuckDB view from the Parquet file
con.execute(f"""
CREATE VIEW parking_data AS
SELECT * FROM parquet_scan('{parquet_file}');
""")
print("View 'parking_data' created from Parquet.")

# Run and optionally save result of each query
for i, query in enumerate(queries, start=1):
    query = query.strip()
    if not query:
        continue  # Skip empty queries

    print(f"\n▶ Running Query {i}:\n{query}")
    try:
        # Try running the query
        result = con.execute(query)

        # Try fetching the result as a DataFrame
        try:
            df = result.fetchdf()
            if not df.empty:
                filename = f"query_{i}.csv"
                output_path = os.path.join(output_folder, filename)
                df.to_csv(output_path, index=False)
                print(f" Saved result to {output_path}")
            else:
                print(f" Query {i} executed successfully, but returned no rows.")
        except duckdb.CatalogException:
            # Query executed, but doesn't return a result set
            print(f" Query {i} ran successfully (no result to save).")
    except Exception as e:
        print(f" Error in Query {i}: {e}")
