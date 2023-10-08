from pyspark.sql import SparkSession
from dotenv import load_dotenv
from .clean_data import clean
from .data_convert import convert


def create_spark_session():
    """Create a Spark Session"""
    # TODO: use env variables later on.
    _ = load_dotenv()
    return SparkSession\
        .builder\
        .appName("OceanDB-Backend")\
        .master("local[2]")\
        .getOrCreate()
    

class FileLoader:
    def __init__(self, spark):
        self.spark = spark

    def load_excel(self, file_path):
        """
        Load an Excel file and return the schema of the DataFrame and its schema.

        Parameters:
            file_path (str): Path to the Excel file.

        Returns:
            pyspark.sql.types.StructType: Schema of the DataFrame.
        """
        df = self.spark.read.format("com.crealytics.spark.excel") \
            .option("location", file_path) \
            .option("useHeader", "true") \
            .load()
        return df,df.schema

    def load_csv(self, file_path):
        """
        Load a CSV file and return the schema of the DataFrame.

        Parameters:
            file_path (str): Path to the CSV file.

        Returns:
            pyspark.sql.types.StructType: Schema of the DataFrame.
        """
        df = self.spark.read.option("header", "true") \
            .option("inferSchema", "true") \
            .csv(file_path)
        return df,df.schema
