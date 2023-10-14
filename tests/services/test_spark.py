# go three folders up
import logging

from ...app.services.spark_oceandb import FileLoader, SparkSession


class TestLoadData:
    def load_excel(file_path: str = './data/SaleData.xlsx'):
        """
            # Test file loading functionality
            # Default dest file provided
        """
        logging.info('Starting Spark Session!')
        try:
            spark = FileLoader(SparkSession())
            # load excel:Returns dataframe and its schema
            _, schema = spark.load_excel(file_path)
            logging.info('Code Executed Successfully')
        except Exception as e:
            logging.warning(e)
