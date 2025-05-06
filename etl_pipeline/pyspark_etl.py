# Sample PySpark ETL script
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("API_Event_ETL").getOrCreate()

df = spark.read.json("path_to_raw_json")
clean_df = df.dropna(subset=["event_id", "timestamp"])
clean_df.write.mode("overwrite").parquet("path_to_processed_data")
