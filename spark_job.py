from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

# Step 1: Start Spark session
spark = SparkSession.builder \
    .appName("AirportParkingSpark") \
    .config("spark.sql.session.timeZone", "UTC") \
    .getOrCreate()

# Step 2: Load and cache the Spark-compatible Parquet
df = spark.read.parquet("airport_parking_dataset/final_output_spark.parquet").cache()

# Step 3: Optional SQL view for running SQL queries
df.createOrReplaceTempView("parking_events")

# Step 4: Revenue by zone
zone_revenue = df.groupBy("zone_id").agg(_sum("paid_amount").alias("total_revenue"))

print("=== Revenue by Zone ===")
zone_revenue.show()

# Step 5: Print execution plan
print("\n=== Execution Plan ===")
df.explain(True)

# Step 6: Pause so Spark UI stays open
input("\nOpen http://localhost:4040 to view Spark UI. Press Enter to stop...")

# Step 7: Stop Spark session
spark.stop()
