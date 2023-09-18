from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("BasicDataCleaning") \
    .getOrCreate()

# Load the dataset (assuming it's a CSV file)
# Replace 'path_to_your_file.csv' with the actual file path
file_path = "path_to_your_file.csv"
df = spark.read.option("header", "true").csv(file_path)

# Display column names
print("Column names:")
df.printSchema()

# Display basic information about the DataFrame
print("Basic DataFrame information:")
df.show()

# Stop the Spark session
spark.stop()