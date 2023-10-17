# go three folders up

from ...app.services.spark_oceandb import FileLoader, SparkSession


class TestLoadData:
    def test_load_excel(file_path: str = './data/SaleData.xlsx'):
        """
            # Test file loading functionality
            # Default dest file provided
        """
        spark = FileLoader(SparkSession())
        # load excel:Returns dataframe and its schema
        _, schema = spark.load_excel(file_path)
        return schema
