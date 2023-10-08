# go three folders up
import logging
from ...app.services import spark_oceandb as sp



logging.info("Starting Spark Session!")
spark = sp.create_spark_session()
logging.info('Code Executed Successfully')