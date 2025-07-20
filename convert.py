import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.read_parquet("airport_parking_dataset/final_output.parquet")

# Convert timestamp to ms and save
table = pa.Table.from_pandas(df, preserve_index=False)
pq.write_table(table, "airport_parking_dataset/final_output_spark.parquet", coerce_timestamps="ms")
