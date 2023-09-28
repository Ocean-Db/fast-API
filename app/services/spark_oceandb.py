from pyspark.sql import SparkSession
from dotenv import load_dotenv
from .clean_data import clean
from .data_convert import convert


def create_spark_session():
    """Create a Spark Session"""
    _ = load_dotenv()
    return (
        SparkSession
        .builder
        .appName("OceanDB-Backend")
        .master("local[5]")
        .getOrCreate()
    )
