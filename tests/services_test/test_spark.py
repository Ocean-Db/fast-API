# go three folders up
import logging
from ...app.services.spark_oceandb import *



logging.info("Starting Spark Session!")
try:
    spark = FileLoader(SparkSession())
    # load excel:Returns dataframe and its schema
    _,schema = spark.load_excel("./data/SaleData.xlsx")
    logging.info('Code Executed Successfully')
except Exception as e:
    logging.warning(e)